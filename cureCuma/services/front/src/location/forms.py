from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator

class CreateLocationForm(FlaskForm):
    """created Location first time"""

    # hidden field
    created = StringField('created')
    name = StringField('name')
    user_id = StringField('user_id', )
    category = StringField('category', )

    # regular field
    adress = StringField('Adress', validators=[DataRequired(), Length(min=2, max=20)])
    postcode = StringField('Code Postal', validators=[DataRequired(), Length(min=5, max=5)])
    town = StringField('Ville', validators=[DataRequired()])

    submit = SubmitField('Go')
