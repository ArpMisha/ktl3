from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import login_required
import models 
from .forms import IsForm
from app import db



task = Blueprint('task', __name__, template_folder='templates')

@task.route('/task')
@login_required
def index():
    tasks = models.iss.query.all()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(tasks)
    return render_template('task/index.html')

@task.route('/task_create', methods=['POST'])
@login_required
def task_create():
    user_input = request.get_json()
    form = IsForm(data=user_input)
    if form.validate():
        task = models.iss(kr_name = form.kr_name.data, name = form.name.data, kategor = form.kategor.data, tip = form.tip.data)
        db.session.add(task)
        db.session.commit()
        return jsonify(task)
    return redirect(url_for('task.index')) 


@task.route('/task_search', methods=['POST'])
@login_required
def task_search():
    user_input = request.get_json().get('kr_name')
    q = models.iss.query.filter(models.iss.kr_name == user_input).all()
    return jsonify(q)
  




   

   






    