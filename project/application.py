from flask import Flask, render_template, request, redirect
import matplotlib.pyplot as plt
from cs50 import SQL

# Instantiating Flask
app = Flask(__name__)

# Acquiring the database
db = SQL("sqlite:///bvsElections.db")

# Security Key
secKey = "BVS2020"

# Count of the total no of voters
cVoters = 0

# All the positions
pos = ["HEAD BOY", "HEAD GIRL", "SPORTS CAPTIAN", "ASST. HEAD BOY", "ASST. HEAD GIRL", "SEASURFERS HOUSE CAPTAIN",
        "STORMCHASERS HOUSE CAPTAIN", "TRAILBLAZERS HOUSE CAPTAIN", "TERRAFORMERS HOUSE CAPTAIN", "CULTURAL SECRETARY",
        "CREATIVE HEAD", "TECHNOLOGY HEAD", "COMMUNICATIONS HEAD", "COMMUNITY AFFAIRS HEAD"]

# ----------------------------------------------------------------------------------------------------

# Home Route
# Access to ADMIN and STUDENT
@app.route("/")
def home():
    return render_template("home.html")

# ----------------------------------------------------------------------------------------------------

# Logging into the administrator
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    else:
        usrName = request.form.get("username")
        usrPasswd = request.form.get("password")

        if not usrName or not usrPasswd:
            return render_template("apology.html", message = "Username or Password was left blank")

        res = db.execute("select * from users where name == ? and hash == ?", usrName, usrPasswd)
        if len(res) != 1:
            return render_template("apology.html", message = "Entered Username or Password was incorrect")

        return render_template("admin.html")

# ----------------------------------------------------------------------------------------------------

# Registering new into the administrator
@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    else:
        usrName = request.form.get("username")
        usrPasswd = request.form.get("password")
        usrConf = request.form.get("confirmation")
        usrSecKey = request.form.get("securityKey")

        if not usrName or not usrPasswd or not usrConf or not usrSecKey:
            return render_template("apology.html", message = "Entered credentials were invalid or left blank")

        res = db.execute("select * from users where name == ?", usrName)
        if len(res) != 0:
            return render_template("apology.html", message = "Entered Username was already taken")

        elif usrPasswd != usrConf:
            return render_template("apology.html", message = "Entered password do not match")

        elif secKey != usrSecKey:
            return render_template("apology.html", message = "Entered dosent match")

        db.execute("insert into users (name, hash) values (?, ?)", usrName, usrPasswd)
        return redirect("/login")

# ----------------------------------------------------------------------------------------------------

# Admin Route
# Access to SETUP, UPDATE, RESULTS AND RESET
@app.route("/admin")
def admin():
    return render_template("admin.html")

# ----------------------------------------------------------------------------------------------------

# Setup Route
@app.route("/setup", methods = ["GET", "POST"])
def setup():
    if request.method == "GET":
        return render_template("setup.html", pos = pos)

    else:
        pName = request.form.get("pos")
        nName = request.form.get("nName")

        if not pName or not nName:
            return render_template("apology.html", message = "Postion name or Nominee name were left blank")

        res = db.execute("select * from nominees where name == ?", nName)
        if res:
            return render_template("apology.html", message = "Nominee has already nominated himself for a position")

        db.execute("insert into nominees (name, position, votes) values (?, ?, ?)", nName, pName, 0)
        return redirect("/setup")

# ----------------------------------------------------------------------------------------------------

# STATS ROUTE
@app.route("/status")
def status():
    nomProf = db.execute("select * from nominees")
    return render_template("view_stats.html", nominees = nomProf)

# ----------------------------------------------------------------------------------------------------

# UPDATE ROUTE
@app.route("/update", methods = ["GET", "POST"])
def update():
    if request.method == "GET":
        return render_template("update.html", pos = pos)

    else:
        pName = request.form.get("pos")
        nName = request.form.get("nName")

        if not pName or not nName:
            return render_template("apology.html", message = "Either of the textboses were left blank")

        # Checking for validity
        res = db.execute("select * from nominees where name == ? and position == ?", nName, pName)
        if not res:
            return render_template("apology.html", message = "The entered credentials are invalid please check")

        # Acquiring the ID to reset the ids for all the nominees
        idVal = res[0]["id"]
        totalCandidates = db.execute("select count(*) as count from nominees")[0]["count"]

        # Removing the nominee
        db.execute("delete from nominees where name == ? and position == ?", nName, pName)

        # Updating the ID's of all the nominees
        for i in range(idVal, totalCandidates + 1):
            db.execute("update nominees set id = ? where id == ?", i, i + 1)

        return redirect("/update")

# --------------------------------------------------------------------------------------------------------

# Result Route
@app.route("/result")
def result():
    # List of all the winners with accordance to the positions
    winners = []

    for i in pos:
        votes = db.execute("select max(votes) as votes from nominees where position == ?", i)[0]["votes"]
        name = db.execute("select name from nominees where votes == ? and position == ?", votes, i)

        if len(name) != 1:
            ls = [i["name"] for i in name]
            winners.append({"name": ls, "position": i, "votes": votes, "len": len(name)})

        else:
            winners.append({"name": name[0]["name"], "position": i, "votes": votes, "len": len(name)})

    return render_template("result.html", winners = winners, cVoters = cVoters)

# ----------------------------------------------------------------------------------------------------

# Reset Route
@app.route("/reset")
def reset():
    # Deleting all the records for all
    db.execute("delete from nominees")

    return redirect("/admin")

# ----------------------------------------------------------------------------------------------------

# Student Route to Start Voting
# Start voting for all the present cofigurations
@app.route("/vote", methods = ["GET", "POST"])
def vote():
    if request.method == "GET":
        # Acquiring all the positions
        hb = db.execute("select name from nominees where position == ?", pos[0])
        hg = db.execute("select name from nominees where position == ?", pos[1])
        sc = db.execute("select name from nominees where position == ?", pos[2])
        asplb = db.execute("select name from nominees where position == ?", pos[3])
        asplg = db.execute("select name from nominees where position == ?", pos[4])
        ssc = db.execute("select name from nominees where position == ?", pos[5])
        scc = db.execute("select name from nominees where position == ?", pos[6])
        tbc = db.execute("select name from nominees where position == ?", pos[7])
        tfc = db.execute("select name from nominees where position == ?", pos[8])
        cs = db.execute("select name from nominees where position == ?", pos[9])
        ch = db.execute("select name from nominees where position == ?", pos[10])
        th = db.execute("select name from nominees where position == ?", pos[11])
        comh = db.execute("select name from nominees where position == ?", pos[12])
        comaf = db.execute("select name from nominees where position == ?", pos[13])

        return render_template("vote.html", hb = hb, hg = hg, sc = sc, asplb = asplb, asplg = asplg,
        ssc = ssc, scc = scc, tbc = tbc, tfc = tfc, cs = cs, ch = ch, th = th, comh = comh, comaf = comaf)

    else:
        # Inserting all the values for the respective nominees
        vals = ["hbNom", "hgNom", "sNom", "asplbNom", "asplgNom", "ssNom", "scNom",
        "tbNom", "tfNom", "csNom", "chNom", "thNom", "comhNom", "comafNom"]

        # Updating the number of voters
        cVoters += 1

        for i in vals:
            val = request.form.get(i)
            if val.split()[0] == "Select":
                return render_template("apology.html", message = "One of the positions was left unselected")

            else:
                # Fetching current number of votes
                cVotes = db.execute("select votes from nominees where name == ?", val)[0]["votes"]
                cVotes += 1

                # Updating the votes
                db.execute("update nominees set votes = ? where name == ?", cVotes, val)

        else:
            return redirect("/vote")

# ----------------------------------------------------------------------------------------------------

# Running the webserver from terminal
if __name__ == "__main__":
	app.run()

else:
	quit()

# ----------------------------------------------------------------------------------------------------