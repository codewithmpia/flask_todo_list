from datetime import datetime

from .settings import db


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow())

    def __str__(self):
        return self.name