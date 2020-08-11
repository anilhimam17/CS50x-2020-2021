# All the imports that are required for flask to function
from flask import Flask, render_template, request

# Intialisation of flask to run application.py as the source file
app = Flask(__name__)

# The home route
@app.route("/")
def home():
    return render_template("home.html")

# Creating a new route to be welcomed after submitting the required answers
# Here the /hello route is activated only after the user activates the form action
@app.route("/hello")
def hello():
    # Acquiring the name from the html
    name = request.args.get("name")

    # To respond to empty imput from the user
    if not name:
        return render_template("faliure.html")
    return render_template("hello.html", name = name)