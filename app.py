from flask import Flask , request ,render_template
from uuid import UUID

app = Flask(__name__)


@app.route("/")
def home():
    details = {
        "name" : "govinda chalaune",
        "age" : 24,
        "city" : "lamki"
    }
    return render_template("index.html",details=details)
    





if __name__ == "__main__":
    app.run(debug=True)