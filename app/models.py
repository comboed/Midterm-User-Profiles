from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    profile_picture = db.Column(db.String(120), default='default.png')

    def __repr__(self):
        return f'<User {self.username}>'
