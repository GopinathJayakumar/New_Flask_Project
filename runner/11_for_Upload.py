# Scenario 10:- Upload

from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from runner.db_module.TestData import Register_DB
from runner.db_module.Data_Base import DataBaseFile
import os

app = Flask(__name__)

folder = "/Users/mac/Workspace/Server"
extensions = set(['txt', 'png', 'jpg', 'jpge'])


def upload(filename):
    return '.' in filename and filename.rsplit('.')[1].lower() in extensions


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('USERNAME') == 'admin' and request.form.get('PASSWORD') == 'password':
            return render_template("homepage.html")
        else:
            alert = "invalid Credential"
            return render_template("loginpage.html", alert=alert)
    return render_template("loginpage.html")


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        print(file)
        if file.filename == '':
            return redirect(request.url)
        if upload(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(folder, file.filename))
            return redirect(request.url)
    return render_template("homepage.html")


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        fname = request.form.get("FNAME")
        lname = request.form.get('LNAME')
        email = request.form.get('EMAIL')
        password = request.form.get('PWD')
        # print(fname, lname, email, password)
        obj = Register_DB(f_name=fname, l_name=lname, email=email, pwd=password)

        con = db_obj.get_connection()
        db_obj.create_table(con, 'register')
        db_obj.insert_records(con, "register", obj)
        db_obj.close_connect(con)

    return render_template("register.html")


if __name__ == "__main__":
    db_obj = DataBaseFile('Register.db')
    app.run(debug=True, port=5010)
