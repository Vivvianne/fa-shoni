from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_secure = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
    contact = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    adress = db.Column(db.String(255))
    
    @classmethod
    def get_profile(cls, id):
      quiz = Profile.query.filter_by(id=id).first()
      return profile

    def save_profile(self):
       db.session.add(self)
       db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
   

    def __repr__(self):
        return f'User {self.name, bio, adress, contact}'

class Subscription(db.Model):
    __tablename__ = 'subscription'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def save_email(self):
        db.session.add(self)
        db.session.commit()
   
    def __repr__(self):
        return f'Subscription {self.email}'