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

if __name__ == "__main__":
    app.run(debug=True)