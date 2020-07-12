# Scenario 2:- for route

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Login Page"


@app.route('/home')
def home():
    return "Welcome to Home Page"


if __name__ == "__main__":
    app.run(debug=True, port=5002)