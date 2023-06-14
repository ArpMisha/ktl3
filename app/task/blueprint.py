from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import login_required
import models 
from .forms import IsForm
from app import db



task = Blueprint('task', __name__, template_folder='templates')
        

@task.route('/task')
@login_required
def index():
    tasks = iss.query.all()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(tasks)
    return render_template('task/index.html')


@task.route('/task_create', methods=['POST'])
@login_required
def create_task():
    user_input = request.get_json()
    form = IsForm(data=user_input)
    if form.validate():
        tasks = models.iss(kr_name=form.kr_name.data, name=form.name.data)
        db.session.add(tasks)
        db.session.commit()
        return jsonify(tasks)
    return redirect(url_for('task.index'))



   

   






    