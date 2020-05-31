from flask import Blueprint
from flask import render_template,redirect,url_for,request
from institute.user.form import Register,Login
from institute.models import User
from institute import db
from flask import flash
from flask_login import current_user,login_required,logout_user,login_user


user= Blueprint('user', __name__)

@user.route("/register",methods=['GET','POST'])
def register():
    form=Register()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password = form.password.data,)
        db.session.add(user)
        db.session.commit()
        flash (f"Your account is created please login now","success")
        return redirect(url_for('login'))
    return render_template("register.html",form=form)


@user.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated :
        return redirect(url_for('home'))
    form=Login()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f"login is unsuccessfull check email and password","danger")
    return render_template("login.html",form=form)


@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

