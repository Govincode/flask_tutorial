from flask import Flask , request ,render_template,redirect,url_for,flash,session,jsonify
from uuid import UUID
import os
from dotenv import load_dotenv
from auth.routes import auth
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"





db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(150), nullable = False)
    age = db.Column(db.Integer)


    



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


@app.route("/create_user",methods=["POST"])
def createUser():
    Data = request.get_json()
    name = Data.get("name")
    email = Data.get("email")
    age = Data.get("age")
    User = Users(
        name = name,
        email = email,
        age = age
    )
    db.session.add(User)
    db.session.commit()

    return jsonify({
        "message" : "User created successfuly",
        "name" : name,
        "email" : email,
        "age" : age

    })



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)