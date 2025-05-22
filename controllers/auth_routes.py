from app import app
from flask import render_template, request, redirect, url_for, flash, session
from controllers.database import db
from controllers.models import *
from datetime import datetime


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email_id']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if not user:
            # raising that user not found
            return render_template('login.html')
        
        if user.password != password:
            # raising that password is incorrect
            return render_template('login.html')
        
        session['email']=email

        #rasise confirmation that user is logged in
        return redirect('/')

    return render_template('login.html')

@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
        # raising confirmation that user is logged out
    else:
        # raising confirmation that user is not logged in
        pass
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    if request.method == 'POST':
        email = request.form['email_id']
        password = request.form['password']
        mobile_number = request.form['mobile']
        address = request.form['address']
        dob = request.form['dob']

        #data vaildation

        if not email or not password:
            # raise email and password required
            print("email and password required")
            return render_template('register.html')
        
        if mobile_number and len(mobile_number) != 10:
            # raise mobile number should be 10 digits
            print("mobile number should be 10 digits")
            return render_template('register.html')
        
        if len(password) < 8:
            # raise password should be 8 characters
            print("password should be 8 characters")
            return render_template('register.html')
        
        if dob:
            dob = datetime.strptime(dob, '%Y-%m-%d').date()

        user = User.query.filter_by(email=email).first()
        if user:
            # raise email already exists
            return render_template('register.html')
        
        # create user
        user_role = Role.query.filter_by(role_name='user').first()
        new_user = User(
            email=email,
            password=password,
            mobile_number=mobile_number,
            address=address,
            dob=dob,
            role = [user_role]
        )

        db.session.add(new_user)
        db.session.commit()

        # raise confirmation that user is registered
        return redirect('/login')
    



