# Importing dependencies
from flask import Flask, redirect, url_for, render_template, request

# Initialize the app
app = Flask(__name__)

# Defining function for the home page
@app.route('/')
def home():
    return render_template("index.html")

# Defining function for the login page
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    return render_template("login.html")

# Defining function for the user page
@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
