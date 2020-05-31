
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager
from flask_mail import Mail


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SECRET_KEY']='12345'
db=SQLAlchemy(app)

login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT'] = '587'
app.config['MAIL_USE_TLS'] = 'True'
app.config['MAIL_USERNAME'] = 'fortesting.dhruvam@gmail.com'
app.config['MAIL_PASSWORD'] = '7405375337'

mail = Mail(app)

from institute.user.routes import user
from institute.student.routes import student
from institute.course.routes import course
from institute import routes

app.register_blueprint(user)
app.register_blueprint(student)
app.register_blueprint(course)

