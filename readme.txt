1. Installation
Download Python IDE: https://wingware.com/downloads
Install VirtualEnv: pip install virtualenv
    virtualenv env
    python env/Scripts/activate_this.py
Install Flask: pip install Flask
Install Flask SQLAlchemy: pip install flask-sqlalchemy
Install Flask Login: pip install flask-login flask-bcrypt
Install Flask WTF: pip install flask-wtf
Install Flask PyMongo: pip install Flask-PyMongo
Install PyMongo: pip install pymongo
Install Flask MongoAlchemy: pip install Flask-MongoAlchemy
Install GIT: 
    https://git-for-windows.github.io/
    Run commands:
        git config --global user.name "Emma Paris"
        git config --global user.email "eparis@atlassian.com"

======================================================================

2. Git

Download & Install https://git-for-windows.github.io/
Run commands:
    git config --global user.name "Emma Paris"
    git config --global user.email "eparis@atlassian.com"

…or create a new repository on the command line

echo "# cloud" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/tkminh/cloud.git
git push -u origin master

…or push an existing repository from the command line

git remote add origin https://github.com/tkminh/cloud.git
git push -u origin master


accepted
check the .gitignore file, if the subdirectory is ignored.

then try again

git add --all
git commit -am "<commit message>"
git push

======================================================================

3. Create blue print
view > blueprint > login_blueprint.py

(GET as default, POST should have prefix "do_...")

from flask import Flask
from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import redirect
    
login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', form=form)
    return redirect('home')

======================================================================

4. Create form + validation
views > form > login_form.py

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

======================================================================

5. Create html view
template > login.html

{{ form.email.label }}<br>
{{ form.email }}</br>
{% if form.email.errors %}
<ul class="errors">{% for error in form.email.errors %}<li>{{ 
error }}</li>{% endfor %}</ul>
{% endif %}

======================================================================

6. Add blueprint to app.py

======================================================================

7. REST API

======================================================================

8. Database

tblTenant:
    id
    

tblUsers:
    id
    email
    pwd_salt
    pwd_hash
    status (0: not active, 1: activated, -1: block)
    role (0: user, 1 manager, 9: admin)
    acc_type (0: community, 1: advanced, 2: professional)
    ip_address
    last_login
    invited_by
    del
    
tblUserProfiles:
    id
    user_id
    firstname
    lastname
    dob
    address
    phone
    mobile
    skype
    avatar
    cover
    
tblProjects:
    id
    name
    description
    created_date
    creator
    type
    latest_version

tblProjectTeam:
    id
    project_id
    user_id
    status (0: not see, 1: approve, -1: disapproved)
    
tblProjectVersion:
    id
    project_id
    version_name
    
tblTestsuites:
    id
    name
    test_type

tblTestcases:
    id
    project_id
    testsuite_id
    author
    title
    precondition
    steps
    expected_behavior
    
tblTestStatus:
    id
    testcase_id
    test_author
    test_date
    version_status (0:not test, 1: pass, 2: failed) limit duplicate row for every testresult per version
    
tblTestscripts:
    id
    testcase_id
    script
    script_generated
    test_data_id
    test_data_mode
    log
    status
    
tblBug:
    id
    testcase_id
    project_id
    version_id
    author
    name
    description
    priority
    steps
    actual_behavior
    expected_bahavior
    attachments
    comments
    status (0: Closed, 1: Open, 2: Fixed, -1: Reopen)


======================================================================
9. Usecase:

    1- Login to system
    2- Logout 
    3- Register account
    4- Create projects
    5- Create testcases
    6- 

======================================================================

10. Bootstrap

======================================================================

11. Helper + CopyCode








