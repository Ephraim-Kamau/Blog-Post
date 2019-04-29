from flask import render_template,request,redirect,url_for
from . import main
from ..models import Review
from .forms import ReviewForm
from flask_login import login_required


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@main.route('/blog/review/new/<int:id>', methods = ['GET','POST'])
@login_required
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

@main.route('/blog/<int:id>')
def blog(id):

    '''
    View blog page function that returns the blog details page and its data
    '''
    blog = get_blog(id)
    title = f'{blog.title}'
    reviews = Review.get_reviews(blog.id)

    return render_template('blog.html',title = title,blog = blog,reviews = reviews)    