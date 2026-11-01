from flask import Flask , request ,render_template
from uuid import UUID

app = Flask(__name__)

#template inheritance in flask
@app.route("/")
def home():
   return render_template("index.html")

@app.route("/About")
def About():
   return render_template("About.html")

@app.route("/Contact")
def Contact():
   return render_template("Contact.html")   





if __name__ == "__main__":
    app.run(debug=True)