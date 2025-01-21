from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Utenti(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    hashed_password = db.Column(db.String(100), nullable=False)