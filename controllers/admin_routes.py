from app import app
from flask import render_template, request, redirect, url_for, flash, session
from controllers.database import db
from controllers.models import *
from datetime import datetime

@app.route('/')
def home():
    if 'email' in session:
        if session['email'] == 'admin@gmail.com':
            return render_template('admin_home.html')
        else: 
            return render_template('user_home.html')
    else:
        return redirect('/login')
    

@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method =='GET':
        return render_template('add_category.html')
    
    if request.method == 'POST':
        # getting data from the form 
        category_name = request.form['category_name']
        # print(category)
        category_description = request.form['description']

        if not category_name:
            # raise category name required
            print("category name required")
            return render_template('add_category.html')
        
        category = Category.query.filter_by(category_name = category_name).first()

        if category:
            # raise category already exists
            print("category already exists")
            return render_template('add_category.html')
        
        category = Category(
            category_name = category_name,
            category_description = category_description
        )

        db.session.add(category)
        db.session.commit()

        # raise confirmation that category is added
        return redirect('/')

    
