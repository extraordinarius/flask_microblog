from app import db
from hashlib import md5

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.Integer, primary_key=False, unique=True)
	email = db.Column(db.String(120), primary_key=False, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')
	about_me = db.Column(db.String(140))
	last_seen = db.Column(db.DateTime)

	def __init__(self, nickname, email, posts=[], about_me='', last_seen=None):
		self.nickname = nickname
		self.email = email
		self.posts = posts
		self.about_me = about_me
		self.last_seen = last_seen

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id) # Python 3

	def avatar(self, size):
		return 'http://www.gravatar.com/avatar/{}?d=mm&s={}'.format(
					md5(self.email.encode('utf-8')).hexdigest(), size)

	@staticmethod
	def make_unique_nickname(nickname):
		if User.query.filter_by(nickname=nickname).first() is None:
			return nickname
		version = 2
		while True:
			new_nickname = '{}-{}'.format(nickname, str(version))
			if User.query.filter_by(nickname=new_nickname).first() is None:
				break
			version += 1

		return new_nickname

	def __repr__(self):
		return '<User {}'.format(self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # def __init__(self, body, timestamp, user_id):
    # 	self.body = body
    # 	self.timestamp = timestamp
    # 	self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % (self.body)
	
