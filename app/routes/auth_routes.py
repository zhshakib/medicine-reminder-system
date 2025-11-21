from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User

# Blueprint for the AUTH routes
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Hashing the password
        hashed_password = generate_password_hash(password)

        # Creating a new user
        user = User.create(name, email, hashed_password)
        
        flash('Registration successful', 'success')

        # Force he/she to login after Registration
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.get_by_email(email)

        if user and check_password_hash(user["password_hash"], password):
            session['user_id'] = user["id"]
            session['username'] = user["name"]

            return redirect(url_for('index'))

        flash('Invalid email or password', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("auth.login"))