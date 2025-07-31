from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the username (which holds email) already exists
        if User.query.filter_by(username=email).first():
            flash('Email already registered. Please log in.', 'warning')
            return redirect(url_for('auth.login'))

        # Create and store new user
        new_user = User(username=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Registered successfully! Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        session.pop('_flashes', None)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(username=email).first()

        if not user:
            flash('No account found. Please register first.', 'warning')
            return redirect(url_for('auth.register'))

        if check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Update if your route is in 'main'
        else:
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))
