from flask import Flask 
from uuid import UUID

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello world"
    



#URL CONVERTEER
#integer converter
@app.route("/user/<int:id>")
def user(id):
    return f"User id is {id}"

#float converter 
@app.route("/product/<float:amount>")
def product(amount):
    return f"product amount is {amount}"

#string converter
#@app.route("/student/<string:name>")
#def student(name):
 #   return f"student name is {name}"

#path converter 
@app.route("/file/<path:file_path>")
def file(file_path):
    return file_path

#uuid converter
@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)

if __name__ == "__main__":
    app.run(debug=True)