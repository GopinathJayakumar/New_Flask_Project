# Scenario 7:- fetch values frm html to python

from flask import Flask, render_template, request

app = Flask(__name__)


# GET, POST

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.get('USERNAME'))
        print(request.form.get('PASSWORD'))
        return render_template("homepage.html")
    return render_template("loginpage.html")


@app.route('/home')
def home():
    return render_template("homepage.html")


@app.route('/registration')
def registration():
    return "Welcome to SignUp"


if __name__ == "__main__":
    app.run(debug=True, port=5007)
