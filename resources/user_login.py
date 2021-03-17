from flask_restful import Resource, reqparse
from models.user import USERMODEL


class login(Resource):
    parser = reqparse.RequestParser()
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
        user_login_email = USERMODEL.find_by_email(data['email'])
        user_login_password = USERMODEL.check_password(data['password'])
        if not user_login_email or not user_login_password:
            return {
                       'massage': 'Unable to login'
                   }, 400

        user_login_email.updated_at()
        return user_login_email.json()
