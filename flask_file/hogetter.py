from flask import Blueprint,render_template,request
from auth import login_required

bp = Blueprint("hogetter",__name__)

@bp.route("/",methods=["GET"])
@login_required
def index():
    return render_template("index.html")
