from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity
from models.user import USERMODEL


class update(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'age',
        type=int,
        required=True
    )
    @jwt_required()
    def put(self):
        verify_jwt_in_request()
        _id = get_jwt_identity()

        data = self.parser.parse_args()
        user = USERMODEL.find_by_id(_id)
        user.age = data['age']
        user.save_to_db()
        return user.json(), 200
