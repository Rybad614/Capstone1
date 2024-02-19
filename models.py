from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from secret import GENIUS

db = SQLAlchemy()
bcrypt = Bcrypt()
DEFAULT_IMAGE = "https://play-lh.googleusercontent.com/CQri0N-BiyrACHpHPPtITg3TMV5-bZNbAuhjrg-Zpc_mw6tIWZJFPmT8Yr5r4R-xbA=w240-h480-rw"

def connect_db(app):

    db.app = app
    db.init_app(app)


class User(db.Model):
    
    __tablename__ = "users"

    id = db.Column(db.Integer,
                   autoincrement=True)

    username = db.Column(db.String(20),
                         primary_key=True,
                         nullable=False,
                         unique=True)
    password = db.Column(db.Text,
                         nullable=False)
    email = db.Column(db.String(50),
                      nullable=False,
                      unique=True)
    image = db.Column(db.Text,
                      nullable=False,
                      default=DEFAULT_IMAGE)
    bio = db.Column(db.String(50))

    history = db.relationship('History')

    

    @classmethod
    def register(cls, username, pwd, email):
        """Register user with hashed passowrd"""

        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf8")

        return cls(username=username,
                   password=hashed_utf8,
                   email=email)
    

    @classmethod
    def authenticate(cls, username, pwd):
        """Validate user exist and password is correct
        
        Return user if valid
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):

            return u
        else:
            return False


class History(db.Model):

    __tablename__ = "history"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    song_info = db.Column(db.Text,
                          nullable=False)
    suggestion = db.Column(db.Text,
                           nullable=False)
    username = db.Column(db.Text,
                         db.ForeignKey('users.username'))
    user = db.relationship('User')


    @classmethod
    def retrieve(cls, song_info, suggestion, username):
        """save data of recently searched results"""
        
        return cls(song_info=song_info,
                   suggestion=suggestion,
                   username=username)