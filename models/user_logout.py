from db import db


class user_logout_model(db.Model):
    __tablename__ = 'blacklist'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String)

    def __init__(self, token):
        self.token = token

    def add_to_blacklist(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def check_token(cls, token):
        select_all = [x.token for x in cls.query.all()]
        return cls.query.filter_by(token=token).first()
