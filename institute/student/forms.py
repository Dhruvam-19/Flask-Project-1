from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField,SubmitField,FileField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class Studentform(FlaskForm):
    first_name=StringField('First name',validators=[DataRequired()])
    middle_name = StringField('Middle name',validators=[DataRequired()])
    last_name = StringField('Last name',validators=[DataRequired()])
    father_first_name = StringField('Father first name', validators=[DataRequired()])
    father_middle_name = StringField('Father middle name', validators=[DataRequired()])
    father_last_name = StringField('Father last name', validators=[DataRequired()])
    house_number = StringField('House number/appartment number',validators=[DataRequired()])
    st_name = StringField('Street name',validators=[DataRequired()])
    area_name = StringField('Area name',validators=[DataRequired()])
    city_name = StringField('City name',validators=[DataRequired()])
    country_name = StringField('Country name',validators=[DataRequired()])
    phone_number = StringField('Phone number',validators=[DataRequired()])
    res_number = StringField('Residence number',validators=[DataRequired()])
    date_of_birth=DateField('Date of birth',format="%Y-%m-%d")
    gender=StringField('Gender',validators=[DataRequired()])
    school_name=StringField('School name',validators=[DataRequired()])
    education=StringField('Education',validators=[DataRequired()])
    photo=StringField('Photo',default='default.png')
    student_email=StringField('Email id',validators=[DataRequired()])
    proof_photo = FileField('upload document',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Submit')

