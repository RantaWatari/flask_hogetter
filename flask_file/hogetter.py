from flask import Blueprint,render_template,request
from auth import login_required

bp = Blueprint("hogetter",__name__,url_prefix="/hogetter")

@bp.route("/",methods=["GET"])
@login_required
def index():
    return render_template("index.html")


@bp.route("/create",methods=["GET","POST"])
@login_required
def create():
    return render_template("hogetter/hogetter_form.html",command="test")


@bp.route("/delete",methods=["GET","POST"])
@login_required
def delete():
    return render_template("hogetter/hogetter_form.html",command="test")


@bp.route("/update",methods=["GET","POST"])
@login_required
def update():
    return render_template("hogetter/hogetter_form.html",command="test")