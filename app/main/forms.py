from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[length(0, 64)])
    location = StringField('Location', validators=[length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')