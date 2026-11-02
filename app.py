from flask import Flask , request ,render_template,redirect,url_for
from uuid import UUID

app = Flask(__name__)

#template inheritance in flask
@app.route("/")
def home():
   return render_template("index.html")

@app.route("/About")
def About():
   return render_template("About.html")

@app.route("/fail")
def fail():
    return render_template("fail.html")

@app.route("/sucess")
def success():
    return render_template("success.html")



@app.route("/Contact", methods=["GET","POST"])
def Contact():
    if request.method == 'POST':
        username = request.form.get("username")
        fullname = request.form.get("fullname")
        specificSize = request.form.get("sizes")
        if not username:
            return redirect(url_for('fail'))
        if not fullname:
            return redirect(url_for('fail'))
        if not specificSize:
            return redirect(url_for('fail'))

        return redirect(url_for('success')) 
    return render_template("Contact.html",username=username,fullname=fullname,specificSize=specificSize)   





if __name__ == "__main__":
    app.run(debug=True)