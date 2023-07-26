from flask import Blueprint,render_template,request,redirect,url_for,g,Response,stream_with_context
from auth import login_required
from hogetter_db_base import show_db_base_single,show_db_base_all,create_db_base,delete_db_base,update_db_base,generate_hogeet_id
from hogetter_db_drive import generate_content_id,put_db_drive,show_db_drive,delete_db_drive

bp = Blueprint("hogetter",__name__,url_prefix="/hogetter")

@bp.route("/",methods=["GET"])
def index():

    return render_template("index.html", posts = show_db_base_all(), owner = g.user)


@bp.route("/create",methods=["POST"])
@login_required
def create():
    hogeet_text = request.form.get("hogeet") 
    content_file = request.files["content"]

    hogeet_id = generate_hogeet_id(hogeet_text)

    if content_file.filename != "":
        content_id = generate_content_id(hogeet_id, content_file.filename, content_file.content_type)
        put_db_drive(content_id, content_file, content_file.content_type)
    else:
        content_id = None

    create_db_base(hogeet_text, hogeet_id, content_id)

    return redirect(url_for("hogetter.index"))


@bp.route("/<hogeet_id>",methods=["GET"])
@login_required
def hogeet_edit(hogeet_id):
    hogeet_content = show_db_base_single(hogeet_id)
    
    return render_template("hogetter/hogeet_edit.html", post=hogeet_content)



@bp.route("/<hogeet_id>/delete",methods=["GET"])
@login_required
def delete(hogeet_id):

    content_id = show_db_base_single(hogeet_id)["content_id"]
    if content_id != None:
        delete_db_drive(content_id)
    delete_db_base(hogeet_id)
    
    return redirect(url_for("hogetter.index"))


@bp.route("/<hogeet_id>/update",methods=["GET","POST"])
@login_required
def update(hogeet_id):
    hogeet_text = request.form.get("hogeet_text")
    delete_action = bool(request.form.get("delete_content"))
    content_file = request.files["content"]

    content_id = show_db_base_single(hogeet_id)["content_id"]

    if delete_action == True and content_id != None:
        delete_db_drive(content_id)
        content_id = None

    elif content_file.filename != "":

        if content_id != None:
            delete_db_drive(content_id)
        
        content_id = generate_content_id(hogeet_id, content_file.filename, content_file.content_type)
        put_db_drive(content_id, content_file, content_file.content_type)
 
    update_db_base(hogeet_id, hogeet_text, content_id)
    
    return redirect(url_for("hogetter.index"))



################################ Drive #############################################

@bp.route("/drive/<content_id>",methods=["GET"])
def drive_img(content_id):
    if request.method == "GET":

        get_content = show_db_drive(content_id)

        get_content_format = content_id.split(".")[-1]
        get_content = get_content.iter_chunks()
        
        if get_content_format in ["mp4","webm"]:
                        
            return Response(stream_with_context(get_content),content_type=f"video/{get_content_format}")
        elif get_content_format in ["jpeg","png","gif"]:
            return Response(stream_with_context(get_content),content_type=f"image/{get_content_format}")
        else:
            return Response(stream_with_context(get_content),content_type=f"audio/{get_content_format}")

@bp.route("/drive/<content_id>/delete",methods=["GET"])
@login_required
def drive_delete(content_id):
    pass

