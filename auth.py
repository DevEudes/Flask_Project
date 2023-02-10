from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .database import User
from . import db


auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.',category='error')
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)

        return redirect(url_for('main.profile'))





@auth.route('/signup', methods=['GET','POST'])
def signup():

    if request.method == 'GET':
        return render_template('signup.html')
    else:
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        firstname = request.form.get('firstname')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first() 

        if user : 
            flash('This email address already exists 😥', category='error')
            return redirect(url_for('auth.signup'))
            
        elif password != password2 :
            flash('Password don\'t match !! Please retry', category='error')
            return redirect(url_for('auth.signup'))   

        elif len(password) < 8 :
            flash('Your password is don \'t Strong  Password must be greater than 8 characters !!', category='error')
            return redirect(url_for('auth.signup'))

        else:       
            new_user = User(email=email, name=name, firstname=firstname, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash(' 🎊 Congratulations your account has been created 🎉', category='success')

            return redirect(url_for('auth.login'))





@auth.route('/logout')
@login_required
def logout():
    
    logout_user()
    return redirect(url_for('main.index'))