from microblog import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.Integer, primary_key=False, unique=True)
	email = db.Column(db.String(120), primary_key=False, unique=True)

	def __repr__(self):
		return '<User {}'.format(self.nickname)

	
