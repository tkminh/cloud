from flask import Flask
from flask import render_template
from flask_wtf.csrf import CSRFProtect
from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.bcrypt import Bcrypt

from views import userprofile
from views import setup
from views import index
from views import home
from views.login import login
from views.registration import registration

from models import user as users
## ====================================== ##
app = Flask(__name__)
app.config.from_pyfile('config.py')
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return users.User(user_id)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.register_blueprint(setup.setup)
app.register_blueprint(index.index)
app.register_blueprint(userprofile.profile)
app.register_blueprint(login.blueprint)
app.register_blueprint(home.home_bp)
app.register_blueprint(registration)


## ====================================== ##
if __name__ == '__main__':
    app.secret_key = 'testcloud2017'
    app.run(port=5000, debug=True)