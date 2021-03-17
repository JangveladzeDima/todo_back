from db import db
from datetime import datetime
from flask_jwt_extended import create_access_token


class USERMODEL(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    age = db.Column(db.Integer)
    password = db.Column(db.String(100))
    createdAt = db.Column(db.String(100))
    uploadAt = db.Column(db.String(100))

    def __init__(self, name, email, age, password):
        self.name = name
        self.email = email
        self.age = age
        self.password = password
        self.createdAt = datetime.now()
        self.uploadAt = datetime.now()

    def json(self):
        return {
            'age': self.age,
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'createdAt': self.createdAt,
            'updatedAt': self.uploadAt
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def check_password(cls, password):
        return cls.query.filter_by(password=password).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def updated_at(self):
        self.uploadAt = datetime.now()
        self.save_to_db()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()

    def get_access_token(self):
        acces_token = create_access_token(identity=self.id, fresh=True)
        return acces_token
