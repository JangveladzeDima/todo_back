from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from models.delete_tasks import delete_taks_model


class deleted_task(Resource):
    @jwt_required()
    def get(self):
        verify_jwt_in_request()
        owner_id = get_jwt_identity()
        all_tasks = delete_taks_model.query.filter_by(owner=owner_id).all()
        return{
            'count': len(all_tasks),
            'data': [x.json() for x in all_tasks]
        }
