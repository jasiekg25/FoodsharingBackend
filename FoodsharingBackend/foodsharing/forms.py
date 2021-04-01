from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistartionForm(FlaskForm):
    name = StringField('Name', 
                       validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', 
                       validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), 
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')