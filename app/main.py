from app import app
import view 
from task.blueprint import task
from task2.blueprint import task2
from task3.blueprint import task3
from task4.blueprint import task4

app.register_blueprint(task)
app.register_blueprint(task2)
app.register_blueprint(task3)
app.register_blueprint(task4)

if __name__ == '__main__':
	app.run(host = '0.0.0.0')

