from app import app
import view 
from task.blueprint import task
from task2.blueprint import task2

app.register_blueprint(task)
app.register_blueprint(task2)

if __name__ == '__main__':
	app.run(host = '0.0.0.0')

