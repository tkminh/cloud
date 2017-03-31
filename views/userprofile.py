from flask import Blueprint
from flask import render_template


profile = Blueprint('profile', __name__)

@profile.route('/about')
def about():
    return render_template('profile/about.html')

