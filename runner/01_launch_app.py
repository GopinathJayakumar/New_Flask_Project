# Scenario 1:-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Flask world"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
