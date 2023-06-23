from flask import Blueprint,render_template,request
from auth import login_required

bp = Blueprint("hogetter",__name__,url_prefix="/hogetter")

@bp.route("/",methods=["GET"])
@login_required
def index():
    return render_template("index.html")
