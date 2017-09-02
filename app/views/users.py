from flask import Blueprint, render_template
from .. import execProcess

users = Blueprint('users', __name__)

@users.route('/')
def showUsers():
    out, c = execProcess('samba-too user list')
    if c == 0:
        render_template('users.html', userslists=out)

@users.route('/add')
def addUsers():
    pass
