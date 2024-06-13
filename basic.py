from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello" # secret_key is essential to start the session
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3" # configure the sqlite database setting
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False # this is optional setting
app.permanent_session_lifetime = timedelta(minutes=5) # set the permanent

db = SQLAlchemy(app) # set up the database

# define a user class to define the data model to database table user
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True) # unique identification
    name = db.Column(db.String(100)) # if you dont define name, the parameter name is same as variable
    email = db.Column(db.String(200))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def start():
    return render_template("start.html")


@app.route("/register", methods=["POST","GET"])
def register():
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            password = request.form["password"]
            session["password"] = password
        else:
            if "password" in session:
                 password = session["password"]
    else:
        return render_template("register.html")


@app.route("/0")
def level0():
    return render_template("level0.html")


@app.route("/1", methods=["GET"])
def level1():
    if "user" in session:
        return redirect(url_for("2")) # if the session contains information of user, the GET method still stay in login status        
    return render_template("level1.html")


@app.route("/2")
def level2():
    return render_template("level2.html")


@app.route("/3")
def level3():
    return render_template("level3.html")


@app.route("/congrat")
def done():
    return render_template("congra.html")

if __name__ == "__main__" :
    app.run()
