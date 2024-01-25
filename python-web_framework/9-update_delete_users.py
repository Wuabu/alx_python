from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User Model class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

# TO DO: Add your code to connect to the database here

# TO DO: Define your USER Model class here

# TO DO 3: Implement the add_user route
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        new_user = User(name=name, email=email)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully!", 'success')
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding user: {str(e)}", 'error')
        finally:
            db.session.close()

    return render_template('add_user.html')

# TO DO 4: Implement the users route
@app.route('/users', strict_slashes=False)
def display_users():
    users = User.query.all()
    return render_template('users.html', users=users)

# TO DO 5: Implement the update_user route
@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        flash("User not found!", 'error')
        return redirect(url_for('display_users'))

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            flash("Name and email are required fields.", 'error')
        else:
            user.name = name
            user.email = email

            try:
                db.session.commit()
                flash("User updated successfully!", 'success')
            except Exception as e:
                db.session.rollback()
                flash(f"Error updating user: {str(e)}", 'error')
            finally:
                db.session.close()

    return render_template('update_user.html', user=user)

# TO DO 6: Implement the delete_user route
@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        flash("User not found!", 'error')
        return redirect(url_for('display_users'))

    if request.method == 'POST':
        try:
            db.session.delete(user)
            db.session.commit()
            flash("User deleted successfully!", 'success')
        except Exception as e:
            db.session.rollback()
            flash(f"Error deleting user: {str(e)}", 'error')
        finally:
            db.session.close()

        return redirect(url_for('display_users'))

    return render_template('delete_user.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

