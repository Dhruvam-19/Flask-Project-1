
from flask import render_template,redirect,url_for
from institute import  app,mail
from institute.forms import Addmission_form,Payment_form,Request_reset_form,Reset_password_form
from institute.models import User,Addmission,Payment
from institute import db
from flask import flash
from flask_login import current_user,login_required
from flask_mail import Message



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/payment',methods=['GET','POST'])
def payment():
    form=Payment_form()

    if form.validate_on_submit():
        payment=Payment(receipt_date=form.receipt_date.data,amount=form.amount.data,
                        type=form.type.data,cheque_number=form.cheque_number.data,
                        bank_name=form.bank_name.data,branch_name=form.branch_name.data
                        ,cheque_date=form.cheque_date.data)
        db.session.add(payment)
        db.session.commit()
        return redirect(url_for('addmission'))
    else:
       # form.student_name.choices = [(str(st.student_id), st.first_name) for st in Student.query.all()]
        return render_template("payment.html",form=form)






@app.route("/addmission",methods=['GET','POST'])
@login_required
def addmission():
    form = Addmission_form();

    if form.validate_on_submit():
        print("post methods")
        print(form.student_name.data)
        addmission=Addmission(addmission_date=form.addmission_date.data,
                              start_timming=form.start_timming.data,
                              end_timming=form.end_timming.data,
                              days=form.days.data,
                              fees=form.fees.data,
                              student_id=int(form.student_name.data),
                              course_id=int(form.course_name.data))
        
        db.session.add(addmission)
        db.session.commit()

        flash(f"New Addmission is added","success")
        return redirect(url_for('addmission',addmission_id=Payment.addmission_id))
    else:
        print('get method')
        #form.student_name.choices = [(str(st.student_id), st.first_name) for st in Student.query.all()]
        #form.course_name.choices = [(str(co.course_id), co.course_name) for co in Course.query.all()]
        return render_template("addmission.html",form=form)

@app.route("/view_addmission",methods=['GET','POST'])
@login_required
def view_addmission():
    addmission=Addmission.query.all()
    return render_template('view_addmission.html',addmission=addmission)





@app.route("/view_addmission/<int:addmission_id>/delete",methods=['GET','POST'])
@login_required
def delete_addmission(addmission_id):
    info=Addmission.query.get_or_404(addmission_id)
    db.session.delete(info)
    db.session.commit()
    flash(f"addmission is deleted!!","success")
    return redirect(url_for("view_addmission"))


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request', sender='fortesting.dhruvam@gmail.com', recipients=[user.email])
    msg.body = f'''
    To reset your password click the following link.
    {url_for('reset_token',token = token,_external = True)}
    If you did not request this message simply ignore this message.
    '''
    mail.send(msg)


@app.route("/reset_password", methods = ['GET','POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = Request_reset_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instruction to reset your password.','info')
        return redirect(url_for("login"))
    return render_template("reset_request.html", title = 'reset password',form= form)


@app.route("/reset_password/<token>", methods = ['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    user = User.verify_reset_token(token)
    if user is None:
        flash('This is invalid or expire token','warning')
        return redirect(url_for("reset_password"))
    form = Reset_password_form()
    if form.validate_on_submit():
        user.password = form.password.data
        db.session.commit()
        flash(f"Your password has been changed.", "success")
        return redirect(url_for('login'))
    return render_template("reset_token.html", title='Reset password', form=form)



