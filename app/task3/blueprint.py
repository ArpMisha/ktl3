from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_security import login_required
import models 
from app import db
from sqlalchemy import text
from datetime import datetime
import subprocess



task3 = Blueprint('task3', __name__, template_folder='templates')

@task3.route('/task3')
#@login_required
def index():
    return render_template('task3/index.html')

@task3.route('/task3_search', methods=['POST'])
#@login_required
def task3_search():
    user_input = request.get_json().get('name')
    cmd = 'cat' + " " + user_input
    results = subprocess.check_output(cmd, shell=True)
    d = {"info": str(results)}
    return jsonify(d)





  




   

   






    