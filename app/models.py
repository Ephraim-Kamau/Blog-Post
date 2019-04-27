class Blog:
    '''
    Blog class to define Blog objects
    '''
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

class Review:

    all_reviews = []

    def __init__(self, blog_id, title):
        self.blog_id = blog_id 
        self.title = title

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()   

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.blog_id == id:
                response.append(review)

        return response           

