# Scenario 9:- fetch values frm html to python

from flask import Flask, render_template, request  # url_for, redirect
from runner.db_module.TestData import Register_DB
from runner.db_module.Data_Base import DataBaseFile

app = Flask(__name__)


def for_auth():
    con = db_obj.get_connection()
    all_data = db_obj.fetch_records(con, 'select F_name, Pwd from register')
    for name, uname in all_data:
        d[str(name)] = str(uname)



# GET, POST
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        con = db_obj.get_connection()
        d = {}
        all_data = db_obj.fetch_records(con, 'select F_name, Pwd from register')
        for name, uname in all_data:
            d[str(name)] = str(uname)
        ls = [request.form.get('USERNAME'), request.form.get('PASSWORD')]
        print(ls)
        for i in d.items():
            if list(i) == ls:
                print(list(i))
                return render_template("homepage.html")
                break
            else:
                print('from else: ', list(i))
                alert = "invalid Credential"
            return render_template('loginpage.html', alert=alert)
    return render_template("loginpage.html")


@app.route('/home')
def home():
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
    for_auth()
    app.run(debug=True, port=5009)
