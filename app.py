from flask import Flask , request ,render_template
from uuid import UUID

app = Flask(__name__)

#ifelse in flask
@app.route("/")
def home():
   names = ["govinda","Hari","Shyam"]
   return render_template("index.html",names=names)
    





if __name__ == "__main__":
    app.run(debug=True)