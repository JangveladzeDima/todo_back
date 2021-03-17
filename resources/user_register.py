from flask_restful import Resource, reqparse
from models.user import USERMODEL


class registration(Resource):
    parser = reqparse.RequestParser()
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
    parser.add_argument(
        'age',
        type=str,
        required=True
    )

    def post(self):
        data = self.parser.parse_args()

        new_user = USERMODEL.find_by_email(data['email'])
        if new_user:
            return {
                       'massage': "this email already exists"
                   }, 400

        new_user = USERMODEL(**data)
        new_user.save_to_db()
        values = new_user.json()
        values['token'] = new_user.get_access_token()
        return values
