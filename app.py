from flask import Flask , request
from uuid import UUID

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello world"
    

@app.route("/search")
def search():
    name = request.args.get("name","guest")
    course = request.args.get("course","unknown")
    return f"{name} is learning {course}"



if __name__ == "__main__":
    app.run(debug=True)