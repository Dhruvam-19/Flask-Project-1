from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileRequired
from wtforms import IntegerField,StringField,BooleanField,PasswordField,SubmitField,RadioField,SelectField,FileField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from institute.models import Student,Course,User
from wtforms.fields.html5 import DateField



class Addmission_form(FlaskForm):
    addmission_date=DateField('Addmission date',validators=[DataRequired()])
    start_timming=StringField('Start timming ',validators=[DataRequired()])
    end_timming=StringField('End timming',validators=[DataRequired()])
    student_name=SelectField("Student Name :",choices=[(str(st.student_id),st.first_name) for st in Student.query.all()] )
    course_name=SelectField("Course Name:",choices=[(str(co.course_id), co.course_name) for co in Course.query.all()])
    #student_name=StringField('Student Name',validators=[DataRequired()])
    #course_name=StringField('Course Name',validators=[DataRequired()])
    days=StringField('Days',validators=[DataRequired()])
    fees=StringField('Fees',validators=[DataRequired()])
    submit=SubmitField('Submit')


class Payment_form(FlaskForm):
    student_name = SelectField("Student Name :",choices=[(str(st.student_id), st.first_name) for st in Student.query.all()])
    receipt_date=DateField('Receipt Date',validators=[DataRequired()])
    amount=IntegerField('Amount',validators=[DataRequired()])
    type=SelectField('Type:',choices=[('Cash','Cash'),('Cheque','Cheque')])
    cheque_number=StringField('Cheque Number')
    bank_name=StringField('Bank Name')
    branch_name=StringField('Branch Name')
    cheque_date=DateField('Cheque Date')
    submit = SubmitField('Submit')


class Request_reset_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError("There is no account with this email. You must register "
                                  "first")

class Reset_password_form(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')