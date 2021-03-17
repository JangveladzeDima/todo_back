from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user_register import registration

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "asdasdasd"
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()

jwt = JWTManager(app)

api.add_resource(registration, '/user/register')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=9999, debug=True)
