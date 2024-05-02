from flask import Flask, redirect, url_for
from flask_file import auth,hogetter

def create_app():
    app = Flask(__name__)
    app.secret_key ="test"

    app.register_blueprint(auth.bp)
    app.register_blueprint(hogetter.bp)
    
    @app.route("/")
    def top():
        return redirect(url_for("hogetter.index"))
    
    return app

app = create_app()