# Scenario 5:- for naviagting endpoints usign url_for

from flask import Flask, url_for  # imported url_for for navigating another endpoint

app = Flask(__name__)


@app.route('/')
def index():
    return '<a href =' + url_for("registration") + '> Registration </a>'


@app.route('/<path:name>')
def home(name):
    return f"Welcome to {name} Page"


@app.route('/registration')
def registration():
    return "Welcome to SignUp"


if __name__ == "__main__":
    app.run(debug=True, port=5005)
