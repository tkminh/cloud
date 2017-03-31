from flask_wtf import Form
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class RegisterForm(Form):
    email = EmailField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired(), validators.Length(min=6, message="Please choose a password of at least 8 characters")])
    password2 = PasswordField('Confirm Password', validators=[validators.DataRequired(), validators.EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit', [validators.DataRequired()])
    
    