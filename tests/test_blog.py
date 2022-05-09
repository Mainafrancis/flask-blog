import unittest
from app.models import User,Article
from app import db

class BlogTest(unittest.TestCase):
    def setUp(self):
        