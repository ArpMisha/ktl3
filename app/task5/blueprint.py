from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import login_required, current_user
from flask_security.forms import ChangePasswordForm
import models 
from app import db, user_datastore
from sqlalchemy import text
from .forms import UserForm



task5 = Blueprint('task5', __name__, template_folder='templates')

@task5.route('/task5')
@login_required
def index():
    username = current_user.email
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'username': username})
    return render_template('task5/index.html')

 


@task5.route('/task5_create', methods=['POST'])
@login_required
def change_password():
    #user_input = request.get_json()
    form = ChangePasswordForm()
    current_user.set_password(form.new_password.data)
    #if form.validate():
    #user = user_datastore.get_user(current_user.id)
    #user.password = hash_password(form.password.data)
    #user_datastore.put(user)
    db.session.commit()
    return jsonify({'result': 'Ok'}), 200




    

  






  




   

   






    