from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class Register(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(max=30,min=4),])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm password',
                                   validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Submit')

class Login(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),])
    submit=SubmitField('Log in')
    remember_me=BooleanField("Remember me")

