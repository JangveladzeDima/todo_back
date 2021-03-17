from flask_restful import Resource, reqparse
from models.task import TASKMODEL
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity

class get_task_by_id(Resource):
    @jwt_required()
    def get(self, task_id):
        verify_jwt_in_request()
        owner_id = get_jwt_identity()
        all_tasks = TASKMODEL.get_task(task_id, owner_id)
        if not all_tasks:
            return {
                'task not found'
            }, 400
        return {'data': [x.json() for x in all_tasks]}