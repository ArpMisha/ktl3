from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import login_required
import models 
from app import db
from sqlalchemy import text
from datetime import datetime
from .forms import IsForm



task5 = Blueprint('task5', __name__, template_folder='templates')

@task5.route('/task5')
#@login_required
def index():
    return render_template('task5/index.html')

@task5.route('/task5_search', methods=['POST'])
#@login_required
def task5_search():
    user_input = request.get_json().get('kr_name')
    results = models.iss.query.filter(models.iss.kr_name == user_input).all()
    return jsonify(results)

@task5.route('/task5_create', methods=['POST'])
#@login_required
def task5_create():
    user_input = request.get_json()
    form = IsForm(data=user_input)
    if form.validate():
        task = models.iss(kr_name = form.kr_name.data, name = form.name.data, kategor = form.kategor.data, tip = form.tip.data)
        db.session.add(task)
        db.session.commit()
        return jsonify(task)
    





  




   

   






    