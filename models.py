from datetime import datetime
from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Storm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)
    code = db.Column(db.String(50), unique=True)
    ideas = db.relationship('Idea', backref="storm", lazy="dynamic")

    def __repr__(self):
        return f'<Storm id: {self.id}, name: "{self.name}">'


class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    color = db.Column(db.String(20))
    storm_id = db.Column(db.Integer, db.ForeignKey("storm.id"))
    created = db.Column(db.DateTime, default=datetime.now)


    def __repr__(self):
        return f'<Idea id: {self.id}'


