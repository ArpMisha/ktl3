from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import login_required
from models import kkss, iss
from app import db



task = Blueprint('task', __name__, template_folder='templates')


        

@task.route('/task')
@login_required
def index():
    tasks = iss.query.all()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(tasks)
    return render_template('task/index.html')









    