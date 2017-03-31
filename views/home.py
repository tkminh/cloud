from flask import Flask
from flask import Blueprint
from flask import render_template
from flask.ext.login import login_required

home_bp = Blueprint('home', __name__, template_folder= 'templates')

@home_bp.route('/home')
@login_required
def home():
    
    return render_template('home.html')
