# All the imports required for a flask web application
from flask import Flask, render_template, request, redirect

# Initialise a flask web app
app = Flask(__name__)

# All the tasks mentioned in the program
tasks = []

# Add a webpage for the home route
@app.route("/")
def home():
    return render_template("home.html", todoList = tasks)

# Adding a webpage for the tasks route
@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        task = request.form.get("task")
        tasks.append(task)
        return redirect("/")

