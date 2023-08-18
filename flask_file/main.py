from flask import Flask
import auth,hogetter

app = Flask(__name__)
app.secret_key ="test"
app.session_cookie_name="hoggeter_cookie"

app.register_blueprint(auth.bp)
app.register_blueprint(hogetter.bp)

