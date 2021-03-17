from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from models.user import USERMODEL


class get_user(Resource):

    @jwt_required()
    def get(self):
        verify_jwt_in_request()
        _id = get_jwt_identity()
        user = USERMODEL.find_by_id(_id)
        return user.json(), 200
