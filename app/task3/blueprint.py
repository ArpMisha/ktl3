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
    #hostname = request.values.get(hostname)
    cmd = 'ls '
    resualt = subprocess.check_output(cmd, shell=True)
    return subprocess.check_output(cmd, shell=True)
    #return render_template('task3/index.html', resualt=resualt)







  




   

   






    