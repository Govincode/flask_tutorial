from flask import Flask 


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello world"
    
@app.route("/Contact")
def contact():
    return "contact us"  
 
@app.route("/About")
def about():
    return "about us" 

#DYNAMIC ROUTING 
@app.route("/user/<name>")
def user(name):
    return f"User name is {name}"

#MULTIPLE PARAMETER DYNAMIC ROUTING
@app.route("/student/<name>/<course>")
def student(name,course):
    return f"{name} is learning {course}"

if __name__ == "__main__":
    app.run(debug=True)