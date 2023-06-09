from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_required
from models import kkss, iss
from app import db



task = Blueprint('task', __name__, template_folder='templates')


        

@task.route('/task')
@login_required
def index():
    return render_template('task/index.html')









    