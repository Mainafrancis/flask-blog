import unittest
from app.models import User,Article
from app import db

class BlogTest(unittest.TestCase):
    def setUp(self):
        '''
        Sets up the before all tests
        '''
        self.user_admin = User(username='admin',password_hash='admin',email='admin@admin.com')
        self.new_article = Article(article='article1',category='technology',user_id=self.user_admin)