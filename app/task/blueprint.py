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


@task.route('/create_task', methods=['POST'])
@login_required
def create_task():
    user_input = request.get_json()
    form = IsForm(data=user_input)
    if form.validate():
        task = models.iss(kr_name=form.kr_name.data)
        db.session.add(task)
        db.session.commit()
        return jsonify(task)
    return redirect(url_for('task.index'))



   

   






    