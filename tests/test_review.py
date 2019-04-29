from app.models import Review,User
from app import db

def setUp(self):
        self.user_James = User(username = 'Ephraim',password = 'potato', email = 'ephraim@ms.com')
        self.new_review = Review(blog_id=1,blog_title='Blog review',
        blog_review='This is a great post',user = self.user_Ephraim)

def tearDown(self):
        Review.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_review.blog_id,1)
        self.assertEquals(self.new_review.blog_title,'Blog review')
        self.assertEquals(self.new_review.blog_review,'This is a great post')
        self.assertEquals(self.new_review.user,self.user_Ephraim)      

def test_save_review(self):
    self.new_review.save_review()
    self.assertTrue(len(Review.query.all())>0)

def test_get_review_by_id(self):

        self.new_review.save_review()
        get_reviews = Review.get_reviews(1)
        self.assertTrue(len(get_reviews) == 1)                  
