import os
from datetime import datetime as dt
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Acquiring all the transaction wrt the current user
    trans = db.execute("select * from share_log where u_id == ?", session["user_id"])

    # Acquiring the cash left
    profile = db.execute("select * from users where id == ?", session["user_id"])
    rem_cash = profile[0]["cash"]

    # Acquiring the grandtotal
    gtotal = 0
    for i in trans:
        gtotal += i["total"]

    return render_template("index.html", trans = trans, rem_cash = rem_cash, gtotal = gtotal + rem_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "GET":
        return render_template("buy.html")

    else:
        # Acquiring the value of the shares required and the symbol
        sym = request.form.get("symbol")
        shs = int(request.form.get("shares"))

        # Checking for invalids
        if not sym or not shs:
            return apology("The some of the values are missing")

        elif shs < 1:
            return apology("Please enter a valid number of shares")

        # Checking for the validity of the given symbol
        dic = lookup(sym)

        if dic == None:
            return apology("The given symbol dosent exist")

        # Checking whether a user can afford the given number of shares
        profile = db.execute("select * from users where id == ?", session["user_id"])

        # Cash value
        pres_cash = profile[0]["cash"]

        # Share Net Total
        share_price = int(dic["price"]) * shs

        if share_price > pres_cash:
            return apology("You do not have the funds to buy the given number of shares")

        else:
            # Executing the database command to complete the transaction
            res = db.execute("select * from share_log where u_id == ? and symbol == ?", session["user_id"], sym)

            if len(res) > 0:
                pres_shs = 0
                pres_total = 0
                for i in res:
                    pres_shs += i["shares"]
                    pres_total += i["total"]

                db.execute("update share_log set shares = ?, price = ?, total = ? where u_id == ? and symbol == ?", pres_shs + shs, dic["price"], pres_total + share_price, session["user_id"], sym)

            else:
                db.execute("insert into share_log values (?, ?, ?, ?, ?, ?, ?)", session["user_id"], sym, dic["name"], dic["price"], shs, share_price, dt.now())

            # Remaining cash after buying all the shares
            rem_cash = pres_cash - share_price

            # Deduction of amount for the bought shares
            db.execute("update users set cash = ? where id == ?", rem_cash, session["user_id"])

            # Noting the transactions in history
            db.execute("insert into transaction_history values (?, ?, ?, ?, ?)", session["user_id"], sym, shs, dic["price"], dt.now())

            return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    trans = db.execute("select * from transaction_history where u_id == ?", session["user_id"])
    return render_template("history.html", trans = trans)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "GET":
        return render_template("quote.html")

    else:
        # Acquiring the symbol that the user has queried
        sym = request.form.get("symbol")

        # Looking up the data of the given symbol
        dic = lookup(sym)

        if dic == None:
            return apology("The stock that was attempted to be looked up did not actually exist")

        # Rendering quoted.html with all the values acquired
        return render_template("quoted.html", name = dic["name"], price = dic["price"], symbol = dic["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # If the request for register page was a get request
    if request.method == "GET":
        return render_template("register.html")

    # If the request for register page was a post request
    else:

        # Acquiring the username
        usrName = request.form.get("username")
        nameCheck = db.execute("select * from users where username == ?", usrName)

        # Acquiring the password and confirmation
        usrPasswd = request.form.get("password")
        usrConf = request.form.get("confirmation")

        if not usrName or len(nameCheck) > 0:
            return apology("Username was already taken")

        elif not usrPasswd or not usrConf:
            return apology("Passwords was left unfilled")

        elif usrPasswd != usrConf:
            return apology("Passwords entered do not match")

        else:
            # Password Hash value to be stored
            passwdHash = generate_password_hash(usrPasswd, method = "plain")

            # Inserting the user into the database
            db.execute("insert into users (username, hash) values (?, ?)", usrName, passwdHash)

            # Redirecting to the homepage
            return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "GET":
        # Acquiring all the stocks corresponding to the user
        stocks = db.execute("select * from share_log where u_id == ?", session["user_id"])
        return render_template("sell.html", stocks = stocks)

    else:
        # Acquiring the symbol and the number of shares
        sym = request.form.get("symbol")
        shs = int(request.form.get("shares"))

        # Checking for the validity of shares and symbols
        if not sym or not shs:
            return apology("Symbol or shares were left blank")

        symCheck = db.execute("select * from share_log where symbol == ? and u_id == ?", sym, session["user_id"])
        if not symCheck:
            return apology("Shares of the selected symbol were not purchased")

        elif symCheck[0]["shares"] < shs:
            return apology("The entered number of shares exceeds the reserves")

        # Executing the transaction for selling
        upShs = symCheck[0]["shares"] - shs
        price = lookup(sym)["price"]
        total = int(symCheck[0]["total"] - (shs * price))
        db.execute("update share_log set shares = ?, price = ?, total = ? where u_id == ? and symbol == ?", upShs, price, total, session["user_id"], sym)

        # Updating the cash of the user
        cash = db.execute("select * from users where id == ?", session["user_id"])[0]["cash"]
        cash += int(price * shs)
        db.execute("update users set cash = ? where id == ?", cash, session["user_id"])

        # Updating the transaction history
        db.execute("insert into transaction_history values (?, ?, ?, ?, ?)", session["user_id"], sym, -shs, price, dt.now())

        # Redirecting to the home route
        return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


# export API_KEY=pk_0fbdbba0861547369d6942f29eb8d640