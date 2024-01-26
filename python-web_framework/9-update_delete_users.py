from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys

# ... (rest of the code remains the same)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Check for existing user with the same email
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists.', 'error')
            return render_template('add_user.html')

        try:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('users'))
        except Exception as e:
            flash(str(e), 'error')

    return render_template('add_user.html')

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Check for email conflict with other users (excluding the current user)
        other_user = User.query.filter_by(email=email).first()
        if other_user and other_user.id != user_id:
            flash('Email already exists.', 'error')
            return render_template('update_user.html', user=user)

        try:
            user.name = name
            user.email = email
            db.session.commit()
            flash('User updated successfully!', 'success')
            return redirect(url_for('users'))
        except Exception as e:
            flash(str(e), 'error')

    return render_template('update_user.html', user=user)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!', 'success')
    except Exception as e:
        flash(str(e), 'error')
    finally:  # Ensure redirect even if errors occur
        return redirect(url_for('users'))

# ... (rest of the code remains the same)
