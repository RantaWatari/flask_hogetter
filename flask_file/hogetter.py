from flask import Blueprint,render_template,request,redirect,url_for,g
from auth import login_required
from hogetter_db import show_db_text,show_db_text_all,create_db_text,delete_db_text

bp = Blueprint("hogetter",__name__,url_prefix="/hogetter")

@bp.route("/",methods=["GET"])
@login_required
def index():

    return render_template("index.html", posts = show_db_text_all(), owner = g.user)


@bp.route("/create",methods=["POST"])
@login_required
def create():
    hogeet = request.form.get("hogeet")
    create_db_text(hogeet)

    return redirect(url_for("hogetter.index"))


@bp.route("/<hogeet_id>",methods=["GET"])
@login_required
def hogeet_edit(hogeet_id):
    hogeet_content = show_db_text(hogeet_id=hogeet_id)
    
    return render_template("hogetter/hogeet_edit.html",hogeet_content=hogeet_content)



@bp.route("/<hogeet_id>/delete",methods=["GET"])
@login_required
def delete(hogeet_id):
    delete_db_text(hogeet_id=hogeet_id)
    
    return redirect(url_for("hogetter.index"))


@bp.route("/<hogeet_id>/update",methods=["GET","POST"])
@login_required
def update(hogeet_id):
    print("test_update")
    pass
    
    return redirect(url_for("hogetter.index"))