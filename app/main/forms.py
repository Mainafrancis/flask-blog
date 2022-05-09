from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import Required
from ..models import Article,Comment

class ArticleUploadForm(FlaskForm):
    article = TextAreaField('Article',validators=[Required()])
    category = StringField('Title',validators=[Required()])
    submit = SubmitField('Add Article')

class CommentsForm(FlaskForm):
    comment = TextAreaField('comment on the article',validators=[Required()])
    submit = SubmitField('Add Comment')

class UpdateProfile(FlaskForm):
    bio = StringField('About You',validators=[Required()])
    submit = SubmitField('Add Bio')