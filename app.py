from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import datetime, timedelta
import time
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "hello" # secret_key is essential to start the session
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3" # configure the sqlite database setting
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False # this is optional setting

ALLOW_TIME_MINUTES = 2
app.permanent_session_lifetime = timedelta(minutes=ALLOW_TIME_MINUTES) # set the permanent

db = SQLAlchemy(app) # set up the database


# define a hero class to define the data model to database table hero
class Hero(db.Model):
    __tablename__ = 'Hero'
    _id = db.Column("id", db.Integer, primary_key=True) # unique identification
    name = db.Column(db.String(100)) # if you dont define name, the parameter name is same as variable
    password = db.Column(db.String(200))
    modifyTime = db.Column(db.DateTime(timezone=True)) # SQLAlchemy takes charge of datetime value setting 
    expiryTimestamp = db.Column(db.Integer) # timestamp record for expiry time

    def __init__(self, name, password, modifyTime, expiryTimestamp):
        self.name = name
        self.password = password
        self.modifyTime = modifyTime
        self.expiryTimestamp = expiryTimestamp

# function to get the available hero name list
def getHeroNameList():
    restrictedTime = str(round(datetime.now().timestamp())) 
    herolist = Hero.query.filter(Hero.expiryTimestamp < restrictedTime).all()
    return [hero.name for hero in herolist]


@app.route("/", methods=["POST", "GET"])
def start():
    session["hero"] = None
    if request.method == "POST":
        session["allow_time_mins"] = ALLOW_TIME_MINUTES
        return redirect(url_for("register"))
    return render_template("start.html")


@app.route("/register", methods=["POST", "GET"])
def register():    
    session["hero"] = None

    if request.method == "POST":
        # set the session to be permanent first
        session.permanent = True
        # if the request is POST, store the hero and password in session
        hero = request.form["hero"]
        password = request.form["password"]

        found_hero = Hero.query.filter_by(name=hero).first() # query the selected hero from database
        if found_hero:
            # update database record
            found_hero.password = password
            found_hero.modifyTime = datetime.now()
            found_hero.expiryTimestamp = int(round(datetime.now().timestamp())) + ALLOW_TIME_MINUTES * 60
            db.session.commit()

            session["hero"] = hero
            session["password"] = password            
            session["expiryTime"] = found_hero.expiryTimestamp

            # redirect to the view page with session of hero and password
            return redirect(url_for("level0"))
        else:
            heroNames = getHeroNameList()
            return render_template("register.html", heroNames = heroNames)
    else:
        heroNames = getHeroNameList()
        return render_template("register.html", heroNames = heroNames)


@app.route("/about")
def about():
    session["hero"] = None
    return render_template("about.html")


@app.route("/barrier")
def barrier():
    session["hero"] = None
    return render_template("barrier.html")
    

@app.route("/timesup")
def timesup():
    session["hero"] = None
    return render_template("timesup.html")


@app.route("/0")
def level0():
    if "hero" not in session:
        return redirect(url_for("start"))   
    if session["hero"] == None:
        return redirect(url_for("barrier"))       
    session.permanent = False
    return render_template("level0.html")       


@app.route("/1", methods=["POST", "GET"])
def level1():
    if "hero" not in session:
        return redirect(url_for("start"))  
    if session["hero"] == None:
        return redirect(url_for("barrier"))   

    if request.method == "POST":
        # if the request is POST, store the um and pw in session
        nm = request.form["nm"]
        pw = request.form["pw"]
        session["nm"] = nm
        session["pw"] = pw
        if session["nm"] != "username":
            flash("Inside Name field, please enter username")
        elif session["pw"] != "incorrect":
            flash("Your password is incorrect")
        else:
            return redirect(url_for("level2")) # if the session contains correct information of nm and pw, go to Level2
    
    return render_template("level1.html")


@app.route("/oneplusone", methods=["POST", "GET"])
def level2():
    if "hero" not in session:
        return redirect(url_for("start"))  
    if session["hero"] == None:
        return redirect(url_for("barrier"))
    if "nm" not in session or "pw" not in session:
        return redirect(url_for("level0"))
    if request.method == "POST":
        passCount = request.form["passCount"]
        session["passCount"] = passCount
        if "passCount" in session:
            return redirect(url_for("level3")) 
    return render_template("level2.html")    


@app.route("/san", methods=["POST", "GET"])
def level3():
    if "hero" not in session:
        return redirect(url_for("start"))  
    if session["hero"] == None:
        return redirect(url_for("barrier"))
    if "nm" not in session or "pw" not in session:
        return redirect(url_for("level0"))
    if "passCount" not in session:
        return redirect(url_for("level2")) 

    if request.method == "POST":
        # if the request is POST, store the um and pw in session
        hero = request.form["hero"]
        password = request.form["password"]

        if not session["hero"] or not session["password"]:
            flash("Your hero power time is over, mission failed. Please return to the starting point")
        if hero != session["hero"]:
            flash("Your hero name is incorrect, please correct and try again")
        elif password != session["password"]:
            flash("Your password is incorrect, please correct and try again")
        else:
            found_hero = Hero.query.filter_by(name=hero).first() # query the selected hero from database
            if found_hero.modifyTime + timedelta(0, 60*ALLOW_TIME_MINUTES) < datetime.now():
                flash("Your hero power time is over, mission failed. Please return to the starting point")
            else:
                return redirect(url_for("congrat")) # if player give correct information of hero and password, go to congrat, end game    
    return render_template("level3.html")


@app.route("/congrat")
def congrat():
    session["hero"] = None
    return render_template("congrat.html")

if __name__ == "__main__" :
    app.run()
