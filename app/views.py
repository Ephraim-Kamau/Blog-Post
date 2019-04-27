from flask import render_template
from app import app
from .models import review
from .forms import ReviewForm


Review = review.Review

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@app.route('/blog/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    blog = get_blog(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(blog.id,title,review)
        new_review.save_review()
        return redirect(url_for('blog',id = blog.id ))

    title = f'{blog.title} review'
    return render_template('new_review.html',title = title, review_form=form, blog=blog)    

@app.route('/blog/<int:id>')
def blog(id):

    '''
    View blog page function that returns the blog details page and its data
    '''
    blog = get_blog(id)
    title = f'{blog.title}'
    reviews = Review.get_reviews(blog.id)

    return render_template('blog.html',title = title,blog = blog,reviews = reviews)    