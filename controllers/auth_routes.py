from app import app
from flask import render_template, request, redirect, url_for, flash

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')