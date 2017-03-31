from flask import Flask
from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import redirect
from flask import flash
from flask.ext.wtf import Form
from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from models import MockDBHelper as DBHelper
from models import user as users
from application.helper import hash_password

app = Flask(__name__)

DB = DBHelper.MockDBHelper()
pwd_helper = hash_password.PasswordHelper()

blueprint = Blueprint('login', __name__, template_folder= 'templates')

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        email = form.email.data
        pwd = form.password.data
        stored_user = DB.get_user(email)
        if stored_user and pwd_helper.validate_password(pwd, stored_user['salt'], stored_user['hashed']):
            u = users.User(email)
            login_user(u)
            return redirect('home')
        flash("submit ne ku " + email)
    return render_template('login.html', form=form)

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect('home')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])


    