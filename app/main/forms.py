from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo



class PostForm(FlaskForm):
    title=StringField('Enter a title',validators = [DataRequired()])
    author = StringField('Enter your username',validators = [DataRequired()])
    content=StringField('Write your blog',validators = [DataRequired()])
    submit = SubmitField('Sign Up')