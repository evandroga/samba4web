from flask import Blueprint, render_template
from .. import execProcess

gpo = Blueprint('gpo', __name__)

@gpo.route('/')
def showGPO():
    out, c = execProcess(('samba-tool',
                          'gpo',
                          'listall'))
    if c == 0:
        render_template('gpo.html', gpolist=out)

@gpo.route('/add')
def addGPO():
    pass
