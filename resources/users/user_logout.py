from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from models.user_logout import user_logout_model


class logout(Resource):

    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        token = user_logout_model(jti)
        token.add_to_blacklist()
        return {
            'success': True
        }, 200

