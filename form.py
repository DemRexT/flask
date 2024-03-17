from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo 

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    last_name = StringField('last name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])