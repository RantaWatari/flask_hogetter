from flask import Flask, redirect, url_for
import auth,hogetter

app = Flask(__name__)
app.secret_key ="test"

app.register_blueprint(auth.bp)
app.register_blueprint(hogetter.bp)

@app.route("/",methods=["GET","POST"])
def top():
    return redirect(url_for("hogetter.index"))