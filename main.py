from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user_register import registration
from resources.user_login import login
from resources.user_logout import logout

from models.user_logout import user_logout_model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
app.secret_key = "asdasdasd"
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_token_in_blacklist(jwt_header, jwt_payload):
    check = user_logout_model.check_token(jwt_payload['jti'])
    if check:
        return True
    return False

api.add_resource(registration, '/user/register')
api.add_resource(login, '/user/login')
api.add_resource(logout, '/user/logout')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=9999, debug=True)
