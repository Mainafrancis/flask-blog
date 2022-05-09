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

    def tearDown(self):
        '''
        deletes test data tests after every test
        '''
        User.query.delete()
        Article.query.delete()

    def test_check_instance_variables(self):
        '''
        test the instances
        '''
        self.assertEquals(self.new_article.article,'article1')
        self.assertEquals(self.new_article.category,'technology')
        self.assertEquals(self.new_article.user_id,self.user_admin)
                