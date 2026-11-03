from flask import Flask , request ,render_template,redirect,url_for,flash,session
from uuid import UUID
import os
from dotenv import load_dotenv
from auth.routes import auth

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRECT_KEY")

app.register_blueprint(auth)

#flask blueprint
@app.route("/")
def home():
   return render_template("index.html")

@app.route("/About")
def About():
   return render_template("about.html")

@app.route("/contact")
def contactus():
    return render_template("contact.html")

@app.route("/dashboard")
def dashboard():
    username = session.get('username')
    return render_template("dashboard.html",username = username)







if __name__ == "__main__":
    app.run(debug=True)