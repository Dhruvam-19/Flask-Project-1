from flask import Blueprint
import os,secrets,base64
from institute import  app
from flask import render_template,redirect,url_for,request,request,jsonify
from institute.student.forms import  Studentform
from institute.models import Student
from institute import db
from flask import flash
from flask_login import login_required



student = Blueprint('student',__name__)

def save_photo(form_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/id_proof',picture_fn)
    form_picture.save(picture_path)
    return picture_fn

@student.route("/new_addmission",methods=['GET','POST'])
def new_addmission():
    form=Studentform()
    picture_file = ""
    if form.validate_on_submit():
        if form.proof_photo.data:
            picture_file = save_photo(form.proof_photo.data)
        student=Student(first_name=form.first_name.data,middle_name=form.middle_name.data
                           ,last_name=form.last_name.data,father_first_name=form.father_first_name.data,
                           father_middle_name=form.father_middle_name.data,
                           father_last_name=form.father_last_name.data,house_number=form.house_number.data,
                           st_name=form.st_name.data,area_name=form.area_name.data,city_name=form.city_name.data,
                           country_name=form.country_name.data,phone_number=form.phone_number.data,
                           res_number=form.res_number.data,date_of_birth=form.date_of_birth.data,
                           gender=form.gender.data,school_name=form.school_name.data,education=form.education.data,
                           photo=form.photo.data,student_email=form.student_email.data,proof_photo = picture_file)
        db.session.add(student)
        db.session.commit()
        flash(f"Your account is created please login now", "success")
        return redirect(url_for('home'))
    if request.args.get('image_name'):
        image_name=secrets.token_hex(8)+".jpeg";
        os.rename(os.path.join(app.root_path,"static/images/captures",'photo.jpeg'),os.path.join(app.root_path,"static/images/captures",image_name))
        form.photo.data=image_name
    return render_template("new_addmission.html", form=form)

@student.route("/view",methods=['GET','POST'])
@login_required
def view():
    page = request.args.get('page', 1, type=int)
    student = Student.query.paginate(page=page, per_page=4)
    return render_template('view.html',student=student)

@student.route("/view/<int:student_id>")
@login_required
def fullview(student_id):
    student=Student.query.get_or_404(student_id)
    addmission = student.addmissions
    return render_template('full_view.html',student=student, addmission=addmission)


@student.route("/view/<int:student_id>/update",methods=('GET','POST'))
@login_required
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    form = Studentform()
    if form.validate_on_submit():
        student.first_name=form.first_name.data
        student.middle_name = form.middle_name.data
        student.last_name = form.last_name.data
        student.father_first_name = form.father_first_name.data
        student.father_middle_name = form.father_middle_name.data
        student.father_last_name = form.father_last_name.data
        student.house_number=form.house_number.data
        student.st_name=form.st_name.data
        student.area_name=form.area_name.data
        student.city_name=form.city_name.data
        student.country_name=form.country_name.data
        student.phone_number=form.phone_number.data
        student.res_number=form.res_number.data
        student.date_of_birth=form.date_of_birth.data
        student.gender=form.gender.data
        student.school_name=form.school_name.data
        student.education=form.education.data
        student.photo=form.photo.data
        student.student_email=form.student_email.data
        db.session.commit()
        flash(f"Student information is updated", "success")
        return redirect(url_for('view', student_id=student_id))
    elif request.method == 'GET':
        form.first_name.data = student.first_name
        form.middle_name.data = student.middle_name
        form.last_name.data = student.last_name
        form.father_first_name.data = student.father_first_name
        form.father_middle_name.data = student.father_middle_name
        form.father_last_name.data = student.father_last_name
        form.house_number.data = student.house_number
        form.st_name.data = student.st_name
        form.area_name.data = student.area_name
        form.city_name.data = student.city_name
        form.country_name.data = student.country_name
        form.phone_number.data = student.phone_number
        form.res_number.data = student.res_number
        form.date_of_birth.data = student.date_of_birth
        form.gender.data = student.gender
        form.school_name.data = student.school_name
        form.education.data = student.education
        form.photo.data = student.photo
        form.student_email.data = student.student_email
        return render_template("new_addmission.html", title="Update Student information", form=form)


@student.route("/view/<int:student_id>/delete",methods=['GET','POST'])
@login_required
def delete_student(student_id):
    info=Student.query.get_or_404(student_id)
    db.session.delete(info)
    db.session.commit()
    flash(f"Student information is deleted!!","success")
    return redirect(url_for("view"))

@app.route('/photo')
def photo():
    return render_template('photo.html')

@app.route('/_photo_cap')
def photo_cap():
    #form = Studentform()
    photo_base64 = request.args.get('photo_cap')
    header, encoded = photo_base64.split(",", 1)
    binary_data = base64.b64decode(encoded)
    #image_name=secrets.token_hex(8)+".jpeg"
    image_name = "photo.jpeg"

    with open(os.path.join(app.root_path,"static/images/captures",image_name), "wb") as f:
        f.write(binary_data)
    #facial recognition operations
    #response = 'your response'
    #form.photo.data=image_name
    return jsonify(response=image_name)
    #return redirect(url_for("new_addmission"))
