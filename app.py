from flask import Flask, render_template, request, url_for,redirect
import dbfunctions

'''
database_name = "flaskwebapp"
user_name = "postgres"
password = "123"
host_ip = "localhost"
host_port = 5432

conn = psycopg2.connect(database = "flaskwebapp",
                        user = "postgres",
                        password = "123",
                        host = "localhost",
                        port = 5432)

crsor = conn.cursor()

crsor.execute("SELECT * FROM users")

user_records = crsor.fetchall()
print(user_records)

'''



app = Flask(__name__)

users = [
    {
        'username'  : 'admin',
        'firstname' : 'talat',
        'middlename': 'can',
        'lastname'  : 'ayhan',
        'birthdate' : '30-06-1998',
        'email'     : 'asd@asd.com',
        'password'  : '123'
    }
]

@app.route("/")
def firstpage():
    return "<a href='/login'>LOGIN</a>"


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        if dbfunctions.login_success(request.form['name'], request.form['pwd']):
            return redirect(url_for("home"), logged = True)


@app.route("/home/<boolean:logged>")
def home(logged = False):
    if logged:
        return render_template("home.html")
    else:
        return redirect(url_for("login"))



if __name__ == '__main__':
    app.run(debug=True)
