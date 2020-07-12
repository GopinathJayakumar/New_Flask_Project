# Scenario 6:- integrated html with the help of render_template

from flask import Flask, render_template        # imported render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("loginpage.html")


@app.route('/home')
def home():
    return f"Welcome to home Page"


@app.route('/registration')
def registration():
    return "Welcome to SignUp"


if __name__ == "__main__":
    app.run(debug=True, port=5006)
