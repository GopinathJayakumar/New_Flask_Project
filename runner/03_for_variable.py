# Scenario 3:- for variable

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Login Page"


@app.route('/<name>')
def home(name):
    return f"Welcome to {name} Page"


if __name__ == "__main__":
    app.run(debug=True, port=5003)