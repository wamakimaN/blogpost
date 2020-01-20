from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required
from ..models import Post

class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    summary = StringField('Quick Summary', validators=[Required()])
    content = TextAreaField('Content')
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    description = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post')