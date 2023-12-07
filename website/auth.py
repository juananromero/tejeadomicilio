from .models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method== 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login correcto!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('ERROR de password!', category='error')
        else:
            flash('Email no existe!', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method== 'POST':
        email = request.form.get('email')
        nombre = request.form.get('nombre')
        password1 = request.form.get('password1')
        password2= request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('ERROR: Email ya existe!', category='error')
        if len(email) < 4:
            flash("Email mínimo de 4 caracteres.", category="error")
        elif len(nombre) < 4:
            flash("Nombre mínimo de 4 caracteres.", category="error")
        elif password1 != password2:
            flash("Las passwords no coinciden.", category="error")
        elif len(password1) < 7:
            flash("password mínimo de 7 caracteres.", category="error")
        else:
            new_user = User(email=email, nombre=nombre, password=generate_password_hash(password1, method='pbkdf2'))
            db.session.add(new_user)
            db.session.commit()
            flash("Cuenta creada!", category="success")
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    return render_template("register.html", user=current_user)