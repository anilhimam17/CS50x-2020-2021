# Import all the data related to flask
from flask import Flask, render_template, request, redirect

# Import sql fro data abases using cs50
from cs50 import SQL

# Intialising all the code related to flask
app = Flask(__name__)

# Initialsing the database model
db = SQL("sqlite:///registrants.db")

# Home route to display all the people present inside the database
@app.route("/")
def home():
    # SQL query to fetch all the information to be rendered in the homepage
    profile = db.execute("select * from register_val")

    # Rendering the template with all the data that was received
    return render_template("homepage.html", profile = profile)

# Register route for registering new email ids
@app.route("/register", methods = ["GET", "POST"])
def register_page():
    # If the request is get, then render registerpage
    if request.method == "GET":
        return render_template("register.html")

    # If the request is post
    else:
        # Accessing the values
        name = request.form.get("name")

        if not name:
            return render_template("apology.html", message = "Please provide a name")

        email = request.form.get("email")
        if not email:
            return render_template("apology.html", message = "Please provide an email")

        # Storing the values in the database
        db.execute("insert into register_val (name, email) values (?, ?)", name, email)

        # Redirecting the user to the homepage
        return redirect("/")