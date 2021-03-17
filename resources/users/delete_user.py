from flask_restful import Resource
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity, get_jwt
from models.user import USERMODEL
from models.user_logout import user_logout_model


class delete_user(Resource):
    @jwt_required()
    def delete(self):
        verify_jwt_in_request()
        _id = get_jwt_identity()
        user = USERMODEL.find_by_id(_id)
        if not user:
            return{
                'massage': 'Please authenticate.'
            }, 401
        values = user.json()
        user.delete_to_db()
        #delete to blacklist
        jti = get_jwt()["jti"]
        token = user_logout_model(jti)
        token.add_to_blacklist()

        return values

