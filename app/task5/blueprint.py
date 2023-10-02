from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import models 
from app import db, user_datastore
#import pickle


task5 = Blueprint('task5', __name__, template_folder='templates')

@task5.route('/task5')
def index():
    return render_template('task5/index.html')

#@task5.route('/task5_upload', methods=['POST'])
#def upload_file():
#    try:
#        # Получаем JSON-данные из веб-формы
#        data = request.get_json()
#
#        if data:
#            # Сериализуем данные с помощью pickle
#            serialized_data = pickle.dumps(data)
            # Записываем сериализованные данные в файл
#            with open('data.pkl', 'wb') as file:
#                file.write(serialized_data)
            # Отправляем файл обратно в веб-интерфейс
#            return send_file('data.pkl', as_attachment=True)
#        else:
#            return jsonify({'message': 'No JSON data received'})

#    except Exception as e:
#        return jsonify({'error': str(e)})






    

  






  




   

   






    