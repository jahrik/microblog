from app import db
from hashlib import md5


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    # Should return true unless user should not be allowed to authenticate.
    def is_authenticated(self):
        return True

    # True unless users are inactive, for example if they have been banned.
    def is_active(self):
        return True

    # True for fake users that are not supposed to log in to the system.
    def is_anonymous(self):
        return False

    # return a unique identifier for the user, handle difference between Python 2 and 3.
    def get_id(self):
        try:
            return uniconde(self.id) # python 2
        except NameError:
            return str(self.id) # python 3

    # gravitar
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
