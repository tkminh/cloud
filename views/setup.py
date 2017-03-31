from flask import Blueprint
from flask import render_template
from application import dbhandler

setup = Blueprint('setup', __name__)

@setup.route('/setupdb')
def setupdb():
    result = dbhandler.init_db()
    
    return render_template('setup.html', result=result)

@setup.route('/reset')
def reset():
    return reduce('setup.html', result='Reset')
