from flask import Flask, redirect, session, url_for
from flask_file import auth,hogetter

def create_app(test_config=None):
    app = Flask(__name__)
    if test_config is not None: app.config.update(test_config)
    app.secret_key ="test"

    app.register_blueprint(auth.bp)
    app.register_blueprint(hogetter.bp)
    
    @app.route("/")
    def top():
        return redirect(url_for("hogetter.index"))
    
    return app

app = create_app()