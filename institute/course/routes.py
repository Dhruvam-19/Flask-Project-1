from flask import Blueprint
from flask import render_template,redirect,url_for,request
from institute.course.forms import Courseform
from institute.models import Course,Addmission
from institute import db
from flask import flash
from flask_login import login_required


course = Blueprint('course',__name__)

@course.route("/new_course",methods=['GET','POST'])
def new_course():
    form=Courseform()
    if form.validate_on_submit():
        course=Course(course_name=form.course_name.data,course_description=form.course_description.data,
                      course_duration=form.course_duration.data,course_fee=form.course_fee.data,
                      status=form.status.data)
        db.session.add(course)
        db.session.commit()
        flash(f"New course is added","success")
        return redirect(url_for('home'))
    else:
        return render_template("course.html",form=form)

@course.route("/view_course",methods=['GET','POST'])
@login_required
def view_course():
    page = request.args.get('page',1,type = int)
    course=Course.query.paginate(page = page,per_page = 4)
    return render_template('view_course.html', course=course,Addmission=Addmission)

@course.route("/view_course/<int:course_id>")
@login_required
def full_view_course(course_id):
    course=Course.query.get_or_404(course_id)
    addmission = course.addmissions
    return render_template('full_view_course.html', course=course, addmission=addmission )


@course.route("/course/<int:course_id>/update",methods=['GET','POST'])
@login_required
def update_course(course_id):
    course=Course.query.get_or_404(course_id)
    form=Courseform()
    if form.validate_on_submit():
        course.course_name=form.course_name.data
        course.course_fee=form.course_fee.data
        course.course_duration=form.course_duration.data
        course.course_description=form.course_description.data
        course.status=form.status.data
        db.session.commit()
        flash(f"Your course is updated","success")
        return redirect(url_for('view_course',course_id=course_id))
    elif request.method=='GET':
        form.course_name.data=course.course_name
        form.course_fee.data=course.course_fee
        form.course_duration.data=course.course_duration
        form.course_description.data=course.course_description
        form.status.data=course.status
    return render_template("course.html",title="Update Course",form=form)


@course.route("/view_course/<int:course_id>/delete",methods=['GET','POST'])
@login_required
def delete_course(course_id):
    info=Course.query.get_or_404(course_id)
    db.session.delete(info)
    db.session.commit()
    flash(f"course is deleted!!","success")
    return redirect(url_for("view_course"))
