from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator

class CreateUserForm(FlaskForm):
    pseudo = StringField('Pseudo', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Mot de Passe', validators=[DataRequired()])
    conf_password = StringField('Confirmation Mot de Passe', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Go')



class LoginUserForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')