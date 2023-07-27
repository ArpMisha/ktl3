from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import login_required, current_user
import models 
from app import db
from sqlalchemy import text





task4 = Blueprint('task4', __name__, template_folder='templates')

@task4.route('/task4')
@login_required
def index():
    username = current_user.email
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'username': username})
    return render_template('task4/index.html')






  




   

   






    