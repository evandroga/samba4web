from flask import Blueprint, render_template
from .. import execProcess

groups = Blueprint('groups', __name__)

@groups.route('/')
def showGroups():
    out, c = execProcess(('samba-tool',
                          'group',
                          'list'))
    if c == 0:
        render_template('groups.html', groupslist=out)

@groups.route('/add')
def addGroups():
    pass
