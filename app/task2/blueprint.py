from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import login_required
import models 
from app import db
from sqlalchemy import text
from datetime import datetime



task2 = Blueprint('task2', __name__, template_folder='templates')

@task2.route('/task2')
#@login_required
def index():
    return render_template('task2/index.html')

@task2.route('/task2_search', methods=['POST'])
#@login_required
def task2_search():
    user_input = request.get_json().get('kr_name')
    results = models.iss.query.filter(models.iss.kr_name == user_input).all()
    return jsonify(results)





  




   

   






    