from app import app
import view 
from task.blueprint import task

app.register_blueprint(task)

if __name__ == '__main__':
	app.run(host = '0.0.0.0')

