from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app import models

if __name__ == '__main__':
	# app.run(debug=True)
	app.debug = True
	manager.run()
