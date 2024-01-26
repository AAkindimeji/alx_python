from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv["learnakins"]
db_password = sys.argv["Akins@1234"]
db_name = sys.argv["alx_flask_db"]
db_host = '127.0.0.1'

app = Flask(__name__)

# TO DO 1: Configure the Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# TO DO 2: Define the User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This will create the tables

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
