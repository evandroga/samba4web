import subprocess
from flask import Flask
from .auth.login import login
from .views.users import users
from .views.groups import groups
from .views.gpo import gpo

app = Flask(__name__)
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(groups, url_prefix='/groups')
app.register_blueprint(gpo, url_prefix='/gpo')


def execProcess(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    out = process.communicate()[0]
    exitCode = process.returncode
    output = []
    for line in out.split('\n'):
        output.append(line)
    return output, exitCode
