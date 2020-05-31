from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class Courseform(FlaskForm):
    course_name = StringField('Course name',validators=[DataRequired()])
    course_description=StringField('Course discription')
    course_duration=StringField('Course duration',validators=[DataRequired()])
    course_fee=StringField('Course fees',validators=[DataRequired()])
    status=StringField('Status',validators=[DataRequired()])
    submit=SubmitField('Submit')

