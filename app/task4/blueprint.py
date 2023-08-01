from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import login_required, current_user
import models 
from app import db, user_datastore
from sqlalchemy import text
from .forms import UserForm


task4 = Blueprint('task4', __name__, template_folder='templates')

@task4.route('/task4')
@login_required
def index():
    username = current_user.email
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'username': username})
    return render_template('task4/index.html')


@task4.route('/task4_delete', methods=['POST'])
#@login_required
def delete_user():
    username = request.get_json().get('username')
    users = models.User.filter_by(email=username).first()
    db.session.delete(users)
    db.session.commit()
    return jsonify({'result': 'Ok'}), 200


@task4.route('/task4_create')
#@login_required
def create_user():
    user_input = request.get_json()
    form = UserForm(data=user_input)
    if form.validate():
        users = user_datastore.create_user(email=form.email.data, password=form.password.data)
        db.session.commit()
        return jsonify({'result': 'Ok'}), 200
    return redirect(url_for('task4.index')) 

  




   

   






    