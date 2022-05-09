from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    '''
    This class will contain database schema for users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique = True,nullable = False)
    email = db.Column(db.String,unique = True,nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    article = db.relationship('Article',backref='user',lazy = 'dynamic')
    comments = db.relationship('Comment',backref='user',lazy='dynamic')
    password_hash = db.Column(db.String,nullable=False)
    @property
    def password(self):
        '''
        Raises error when someone trys to read the password
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        '''
        Generates password hash
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        '''
        confirms password equal to the password hash during login
        '''
        check_password_hash(self.password_hash,password)

class Article(db.Model):
    '''
    This class will contain the database schema for articles table
    '''
    __tablename__ = 'articles'

    id = db.Column(db.Integer,primary_key = True)
    article = db.Column(db.String)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref='article',lazy='dynamic')

    def save_article(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_article(cls):
        articles = Article.query.all()
        return articles
class Comment(db.Model):
    '''
    This class will contain the schema for comments
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    article_id = db.Column(db.Integer,db.ForeignKey('articles.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    @classmethod
    def get_comments(cls,article_id):
        comments = Comment.query.filter_by(article_id=article_id).all()
        return comments

class Quotes:
    def __init__(self,author,quote):
        '''
        Method to instanciate the quotes class
        '''
        self.author = author
        self.quote = quote

    