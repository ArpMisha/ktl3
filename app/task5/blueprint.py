from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import login_required, current_user
import models 
from app import db, user_datastore, 
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
    data = request.get_json()
    username = data.get('email')
    new_password = data.get('new_password')
    user_datastore.set_password(username, new_password)
    db.session.commit()
    return jsonify({'result': 'Ok'}), 200


    

  






  




   

   






    