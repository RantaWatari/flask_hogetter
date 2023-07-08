from flask import Blueprint,render_template,request,session,redirect,url_for,g,flash
import functools
from auth_db import signup_db,signout_db,get_account
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


bp = Blueprint("auth", __name__,url_prefix="/hogetter")

def login_required(view):
    # 2023.6.21 sessionキーがリクエスト間しか情報を保たないはずなのに、logoutするときはsession.clear()をする。なぜ？
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():

    username = session.get("username")
    if username is None:
        g.user = None
    else:
        g.user = username


def auth_form_check(username:str,password:str):
    error = None        
    if not username:
        error = "Username is required"
    elif not password:
        error = "Password is required"
    elif len(username) <= 0 or 25 <= len(username):
        error = "Username is limit over"
    elif len(password) <= 0 or 20 <= len(password):
        error ="Password is limit over"
    
    return error

@bp.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("auth/auth_form.html",command = "signup")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        error = auth_form_check(username=username,password=password)
        if error != None:
            flash(error)
            return render_template("auth/auth_form.html",command = "signup")
            

        if get_account(username=username) == None:
            signup_db(username=username,password=generate_password_hash(password))
            return render_template("auth/auth_form.html",command = "login")
        
        else:    
            flash(f"User {username} is already exist.")
            return render_template("auth/auth_form.html",command = "signup")


@bp.route("/signout",methods=["GET","POST"])
@login_required
def signout():
    if request.method == "GET":
        return render_template("auth/auth_form.html",command = "signout")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        error = auth_form_check(username=username,password=password)
        if error != None:
            flash(error)
            return render_template("auth/auth_form.html",command = "signout")

        if get_account(username=username) == None:
            flash(f"User {username} is not exist.")
            return render_template("auth/auth_form.html",command = "signout")
        
        elif check_password_hash(get_account(username=username)["password"],password) == False:    
            flash("Password is diffrent.")
            return render_template("auth/auth_form.html",command = "signout")

        else:
            signout_db(username=username)
            return redirect(url_for("auth.logout"))


@bp.route("/login",methods=["GET","POST"])
def login():

    if request.method == "GET":
        return render_template("auth/auth_form.html",command = "login")
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        error = auth_form_check(username=username,password=password)
        if error != None:
            flash(error)
            return render_template("auth/auth_form.html",command = "login")       
       
        if get_account(username=username) == None:
            flash(f"User {username} is not exist.Please signup.")
            return render_template("auth/auth_form.html",command = "signup")
        
        elif check_password_hash(get_account(username=username)["password"],password) == False:    
            flash("Password is diffrent.")
            return render_template("auth/auth_form.html",command = "login")

        else:
            session.clear()
            session["username"] = username

        return redirect(url_for("hogetter.index"))


@bp.route("/logout",methods=["GET"])
@login_required
def logout():
    session.clear()

    return redirect(url_for("hogetter.index"))


