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

    def test_save_article(self):
        '''
        test saving in the db
        '''
        self.new_article.save_article()
        self.assertTrue(len(Review.query.all())>0)

    def test_get_article_by_id(self):
        '''
        tests getting article by id
        '''
        self.new_article.save_article()
        got_article = Article.query.get(1)
        self.assertTrue(len(got_article)==1)