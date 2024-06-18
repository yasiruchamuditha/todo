from flask import render_template, url_for, flash, redirect, request, jsonify
from app import app, db, bcrypt
from forms import RegistrationForm, LoginForm, TaskForm
from models import User, Task
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route("/home")
@login_required
def home():
    tasks = Task.query.filter_by(owner=current_user)
    form = TaskForm()
    return render_template('index.html', title='Home', tasks=tasks, form=form)

@app.route("/add_task", methods=['POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data, owner=current_user)
        db.session.add(task)
        db.session.commit()
        flash('Your task has been added!', 'success')
    return redirect(url_for('home'))

@app.route("/complete_task/<int:task_id>")
@login_required
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        abort(403)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/delete_task/<int:task_id>")
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
