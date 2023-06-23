import datetime
from flask import render_template, flash, redirect, url_for, Markup, session
from flask_login.utils import login_required, login_user, logout_user, current_user

from . import auth_bp
from .forms import LogInForm, SignUpForm
from .models import User

from . import db, bcrypt, login_manager


@auth_bp.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()

    if current_user.is_authenticated:
        flash('not anonymous', 'warning')
        return redirect(url_for('public.index'))

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')

        if User.query.filter_by(email = email).first():
            flash(Markup(f'adres  <b>{email}</b jest w użyciu'), 'danger')
        
        else:
            created_at = datetime.datetime.now()
            user = User(name=name, email=email, password=hashed_password, created_at=created_at)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Pomyślnie utworzono użytkownika.', 'dark')
            return redirect(url_for('public.index'))

    return render_template('auth/signup.html', form=form)


@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LogInForm()

    if current_user.is_authenticated:
        flash('not anonymous', 'warning')
        return redirect(url_for('public.index'))

    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email = email).first()
        
        if user:
            password = form.password.data

            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('public.index'))

            else:
                flash('Niepoprawne hasło.', 'danger')

        else:
            flash(Markup(f'Istnieje już kąto powiązane z tym e-mailem <b>{email}</b>'), 'danger')

    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('cart', None)
    flash('Sesja została zamknięta pomyślnie', 'info')
    return redirect(url_for('public.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)