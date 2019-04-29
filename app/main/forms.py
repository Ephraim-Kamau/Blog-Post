from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Write your comment here',validators=[Required()])
    review = TextAreaField('Blog review', validators=[Required()])
    submit = SubmitField('Submit')