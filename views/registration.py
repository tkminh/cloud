from flask import Flask
from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import redirect

from views.form.register import RegisterForm
from models import MockDBHelper as DBHelper
from application.helper import hash_password

DB = DBHelper.MockDBHelper()
pwd_helper = hash_password.PasswordHelper()

registration = Blueprint('register', __name__, template_folder= 'templates')

@registration.route('/register')
def _register():
    form = RegisterForm()
    return render_template("registration.html", form = form)


@registration.route('/do_register', methods=["POST"])
def _do_register():
    form = RegisterForm()
    if form.validate():
        if DB.get_user(form.email.data):
            form.email.errors.append("Email already exists")
            return render_template('registration.html', form=form)
        salt = pwd_helper.get_salt()
        hashed = pwd_helper.get_hash(form.password2.data + salt)
        DB.add_user(form.email.data, salt, hashed)
        return redirect('home')
    return render_template('registration.html', form=form)