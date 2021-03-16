from flask_restful import Resource, reqparse
from models.user import USER

class registration(Resource):
    parser = reqparse.RequestParser
    parser.add_argument(
        'name',
        type=str,
        required=True
    )
    parser.add_argument(
        'email',
        type=str,
        required=True
    )
    parser.add_argument(
        'password',
        type=str,
        required=True
    )
    def post(self):

        data = self.parser.parse_args()
        new_user = USER.find_by_email(data['email'])
        if new_user:
            return {
                'massage': "this email already exists"
            }, 400
        new_user = USER(**data)
        new_user.save_to_db()
        return {

        }


