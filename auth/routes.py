from flask import Blueprint,request,redirect,url_for,session,render_template


auth = Blueprint("auth",__name__,url_prefix='/auth')




@auth.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
            
        if username == "govinda" and password == "1234":
            session["logged_in"] = True
            session["username"] = "govinda"
            return redirect(url_for('dashboard'))
        return "Invalid username or password"
    return render_template("login.html")



@auth.route('/signup')
def signup():
    pass

@auth.route('/logout')
def logout():
    session.pop("logged_in")
    session.pop("username")
    return redirect(url_for("home"))