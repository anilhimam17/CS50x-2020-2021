# All the imports required for a flask web application
from flask import Flask, render_template, request, redirect, session
from flask_session import Session

''' Here we are importing sessions to give dynamic content with respect ot each of the users '''

# Initialise a flask web app
app = Flask(__name__)

# To disable permanent sessions
app.config["SESSIONS_PERMANENT"] = False

# To set the type of session to files
app.config["SESSION_TYPE"] = "filesystem"

# To initialise the created session
Session(app)

# Add a webpage for the home route
@app.route("/")
def home():
    # To check if the user has the list of todos
    if "todos" not in session:
        # Creating a new todo list
        session["todos"] = []

    # Calling out the ol with the new todos list
    return render_template("home.html", todos = session["todos"])

# Adding a webpage for the tasks route
@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        task = request.form.get("task")
        session["todos"].append(task)
        return redirect("/")

