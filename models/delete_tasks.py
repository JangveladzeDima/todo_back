from db import db
from datetime import datetime


class delete_taks_model(db.Model):
    __tablename__ = 'deleted_tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    completed = db.Column(db.Boolean)
    description = db.Column(db.String(100))
    createdAt = db.Column(db.String(100))
    uploadAt = db.Column(db.String(100))
    owner = db.Column(db.Integer)

    def __init__(self, description, owner):
        self.description = description
        self.completed = False
        self.createdAt = datetime.now()
        self.uploadAt = datetime.now()
        self.owner = owner

    def json(self):
        return {
            'completed': self.completed,
            'id': self.id,
            'description': self.description,
            'owner': self.owner,
            'createdAt': self.createdAt,
            'updatedAt': self.uploadAt
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()
