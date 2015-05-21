import os
import unittest

from config import basedir
from app import app, db
from app.models import User

class TestCase(unittest.TestCase):

	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_avatar(self):
		u = User(nickname='extraordinarius', email='extraordinarius@yahoo.com')
		avatar = u.avatar(128)
		expected = 'http://www.gravatar.com/avatar/0fa72ec2e2b07baee46713b7fce4f9c0?d=mm&s=128'
		assert avatar[0:len(expected)] == expected

	def test_make_unique_nickname(self):
		u = User(nickname='extraordinarius', email='extraordinarius@yahoo.com')
		db.session.add(u)
		db.session.commit()
		nickname = User.make_unique_nickname('extraordinarius')
		assert nickname != 'extraordinarius'

		u = User(nickname=nickname, email='susan@example.com')
		db.session.add(u)
		db.session.commit()

		nickname2 = User.make_unique_nickname('extraordinarius')

		assert nickname2 != 'extraordinarius'
		assert nickname2 != nickname

if __name__ == '__main__':
	unittest.main()
