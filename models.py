# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.sql import func


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # One-to-many relationship with diagnosis history
    diagnosis_history = db.relationship(
        'DiagnosisHistory',
        backref='user',
        lazy=True,
        cascade='all, delete-orphan'
    )

class DiagnosisHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)
    disease = db.Column(db.String(100), nullable=False)
    advice = db.Column(db.Text)
    emergency = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())

