from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Write your comment here',validators=[Required()])
    review = TextAreaField('Blog review')
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Blog title', validators = [Required()])
    description = TextAreaField('Blog description', validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')    

class DeleteBlog(FlaskForm):
    delete=SubmitField("Delete this Blog")

class DeleteComment(FlaskForm):
    delete1=SubmitField("Delete")    