from flask import Blueprint,render_template,request,redirect,url_for
from auth import login_required
from hogetter_db import show_db,create_db

bp = Blueprint("hogetter",__name__,url_prefix="/hogetter")

@bp.route("/",methods=["GET"])
@login_required
def index():
    return render_template("index.html",posts=show_db())


@bp.route("/create",methods=["POST"])
@login_required
def create():
    hogeet = request.form.get("hogeet")
    create_db(hogeet)

    return redirect(url_for("hogetter.index"))


@bp.route("/delete",methods=["GET","POST"])
@login_required
def delete():
    return render_template("hogetter/hogetter_form.html",command="test")


@bp.route("/update",methods=["GET","POST"])
@login_required
def update():
    return render_template("hogetter/hogetter_form.html",command="test")