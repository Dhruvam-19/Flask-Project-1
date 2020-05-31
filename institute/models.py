from institute import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def get_reset_token(self, expire_second=1800):
        s = Serializer(app.config['SECRET_KEY'], expire_second)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    '''@staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    '''

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    middle_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    father_first_name = db.Column(db.String(20), nullable=False)
    father_middle_name = db.Column(db.String(20))
    father_last_name = db.Column(db.String(20))
    house_number = db.Column(db.String(20), nullable=False)
    st_name = db.Column(db.String(30), nullable=False)
    area_name = db.Column(db.String(30), nullable=False)
    city_name = db.Column(db.String(30), nullable=False)
    country_name = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(11), nullable=False)
    res_number = db.Column(db.String(11), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    school_name = db.Column(db.String(30), nullable=False)
    education = db.Column(db.String(30), nullable=False)
    photo = db.Column(db.String(30), nullable=False, default='default.png')
    student_email = db.Column(db.String(120), nullable=False)
    proof_photo = db.Column(db.String(50), nullable=True, default='default.png')
    addmissions = db.relationship('Addmission', backref='student', lazy=True)


class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(20), nullable=False)
    course_description = db.Column(db.Text)
    course_duration = db.Column(db.String(20), nullable=False)
    course_fee = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    addmissions = db.relationship('Addmission', backref='course', lazy=True)


class Addmission(db.Model):
    addmission_id = db.Column(db.Integer, primary_key=True)
    addmission_date = db.Column(db.Date, nullable=False)
    start_timming = db.Column(db.String(15), nullable=False)
    end_timming = db.Column(db.String(15), nullable=False)
    fees = db.Column(db.String(20), nullable=False)
    days = db.Column(db.String(20), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=True)

    payment = db.relationship('Payment', backref='fees', lazy=True)

    def __repr__(self):
        return f"Addmission('{self.course_id}','{self.student_id}','{self.addmission_id}')"


class Payment(db.Model):
    receipt_id = db.Column(db.Integer, primary_key=True)
    receipt_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(10), nullable=False)
    cheque_number = db.Column(db.String(30), nullable=True)
    bank_name = db.Column(db.String(20), nullable=True)
    branch_name = db.Column(db.String(20), nullable=True)
    cheque_date = db.Column(db.Date, nullable=True)
    addmission_id = db.Column(db.Integer, db.ForeignKey('addmission.addmission_id'))

    def __repr__(self):
        return f"Addmission('{self.receipt_id}','{self.receipt_date}','{self.amount}')"
