import unittest
from app.models import Blog, User


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_moureen = User(username='pa', password='papa', email='test@test.com')
        self.new_blog = Blog(id=1, title='Test', content='This is a test blog', user_id=self.user_moureen.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()