from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file
from flask_security import login_required
import models 
from app import db
from sqlalchemy import text
from datetime import datetime
from wand.image import Image as WandImage
import os
import io



task6 = Blueprint('task6', __name__, template_folder='templates')

@task6.route('/task6')
#@login_required
def index():
    return render_template('task6/index.html')


@task6.route('/upload-photo', methods=['POST'])
def process_image():
   # Получаем файл из запроса
    image_file = request.files['photo']
    
    # Открываем изображение с помощью Wand
    with WandImage(file=image_file) as img:
        # Пример обработки - изменение размера изображения
        img.resize(200, 200)
        
        # Сохраняем обработанное изображение в буфер
        processed_image_buffer = io.BytesIO()
        img.save(file=processed_image_buffer)
        processed_image_buffer.seek(0)  # Перемещаем указатель в начало буфера


    return render_template('task6/index.html')


    





  




   

   






    