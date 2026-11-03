from flask import Flask , request ,render_template,redirect,url_for,flash,session
from uuid import UUID
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRECT_KEY"] = os.getenv("SECRECT_KEY")

#template inheritance in flask
@app.route("/")
def home():
   return render_template("index.html")

@app.route("/About")
def About():
   return render_template("about.html")



@app.route("/flashMsg")
def flashMsg():
    return render_template("flashMsg.html")

@app.route("/contact")
def contactus():
    return render_template("contact.html")





@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login",methods = ["POST","GET"])
def login_validation():

        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
        
            if username == "govinda" and password == "1234":
                session["logged_in"] = True
                session["username"] = "govinda"
                return redirect(url_for('dashboard'))
            return "Invalid username or password"
        return render_template(url_for('login'))
       


   

@app.route("/dashboard")
def dashboard():
    logged_in = session.get("logged_in")
    username = session.get("username")
    if not logged_in:
        return redirect(url_for('login'))
    else:
        return render_template("dashboard.html",username = username)

@app.route("/logout")
def logout():
    session.pop("logged_in")
    session.pop("username")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)