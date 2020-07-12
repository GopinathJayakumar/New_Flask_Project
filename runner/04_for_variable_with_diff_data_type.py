# Scenario 4:- for variable with diff data type

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Login Page"


@app.route('/<path:name>')      # <string:name>, <int:name>, <path:name>
def home(name):
    return f"Welcome to {name} Page"


if __name__ == "__main__":
    app.run(debug=True, port=5004)