from flask import Blueprint,render_template,request,redirect,url_for,g
from auth import login_required
from hogetter_db_base import show_db_text_single,show_db_text_all,create_db_text,delete_db_text,update_db_text,generate_hogeet_id
from hogetter_db_drive import generate_content_id,put_db_drive

bp = Blueprint("hogetter",__name__,url_prefix="/hogetter")

@bp.route("/",methods=["GET"])
@login_required
def index():

    return render_template("index.html", posts = show_db_text_all(), owner = g.user)


@bp.route("/create",methods=["POST"])
@login_required
def create():
    hogeet_text = request.form.get("hogeet")
#    content = request.files("content")
#    print(hogeet_text,content.filename)

    hogeet_id = generate_hogeet_id(hogeet_text=hogeet_text)
    #content_id = generate_content_id(hogeet_id=hogeet_id,content_name=content.filename)
    create_db_text(hogeet_text=hogeet_text, hogeet_id=hogeet_id)


    return redirect(url_for("hogetter.index"))


@bp.route("/<hogeet_id>",methods=["GET"])
@login_required
def hogeet_edit(hogeet_id):
    hogeet_content = show_db_text_single(hogeet_id=hogeet_id)
    
    return render_template("hogetter/hogeet_edit.html",hogeet_content=hogeet_content)



@bp.route("/<hogeet_id>/delete",methods=["GET"])
@login_required
def delete(hogeet_id):
    delete_db_text(hogeet_id=hogeet_id)
    
    return redirect(url_for("hogetter.index"))


@bp.route("/<hogeet_id>/update",methods=["GET","POST"])
@login_required
def update(hogeet_id):
    
    hogeet_text = request.form.get("hogeet_text")
    update_db_text(hogeet_id=hogeet_id,hogeet_text=hogeet_text)
    
    return redirect(url_for("hogetter.index"))



################################ Drive #############################################

@bp.route("/drive/put",methods=["GET"])
@login_required
def drive_put():
    pass


@bp.route("/drive/<content_id>",methods=["GET"])
@login_required
def drive_show(content_id):
    pass


@bp.route("/drive/<content_id>/delete",methods=["GET"])
@login_required
def drive_delete(content_id):
    pass

