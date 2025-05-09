from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy 
    # Using Integer for id is incorrect. Its inuberable. Set to string and uisng UUID, Snowflake or other libraries to generate unique id.
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000)) 
