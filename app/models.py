from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.Integer, primary_key=False, unique=True)
	email = db.Column(db.String(120), primary_key=False, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User {}'.format(self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
	