import unittest
from app.models import Blog


class BlogTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_blog = Blog(id, 'First Post', 'Ephraim Kamau')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))    


