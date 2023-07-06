from flask import Blueprint,render_template,request,session,redirect,url_for,g,flash
import functools
from auth_db import signup_db,signout_db,get_account


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


@bp.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("auth/auth_form.html",command = "signup")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        

        error = None        
        if not username:
            error = "Username is required"
        elif not password:
            error = "Password is required"
        else:
            confirm_get_account = get_account(username=username)
            if confirm_get_account != None:
                error = f"User {username} is already exist."


        if confirm_get_account == None:
            signup_db(username=username,password=password)
            return render_template("auth/auth_form.html",command = "login")
        
        flash(error)

        return render_template("auth/auth_form.html",command = "signup")


@bp.route("/signout",methods=["GET","POST"])
@login_required
def signout():
    if request.method == "GET":
        return render_template("auth/auth_form.html",command = "signout")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        signout_db(username=username)

        return redirect(url_for("auth.logout"))


@bp.route("/login",methods=["GET","POST"])
def login():

    if request.method == "GET":
        return render_template("auth/auth_form.html",command = "login")
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if get_account(username=username)["password"] == password:

            session.clear()
            session["username"] = username
        else:
            pass

        return redirect(url_for("hogetter.index"))


@bp.route("/logout",methods=["GET"])
@login_required
def logout():
    session.clear()

    return redirect(url_for("hogetter.index"))


