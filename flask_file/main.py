from flask import Flask,render_template
import auth,hogetter
from auth import login_required

app = Flask(__name__)
app.secret_key ="test"


@app.route("/test",methods=["GET"])
def test():
    return "test"

@app.route("/test/<string>",methods=["GET"])
def test_str(string):
    return f"Test {string}!!"


app.register_blueprint(auth.bp)
app.register_blueprint(hogetter.bp)


