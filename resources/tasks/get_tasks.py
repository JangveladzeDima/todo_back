from flask_restful import Resource, reqparse
from flask import request
from models.task import TASKMODEL
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity


class get_task_by_id(Resource):
    @jwt_required()
    def get(self, task_id):
        verify_jwt_in_request()
        owner_id = get_jwt_identity()
        task_by_id = TASKMODEL.get_task_to_id(task_id, owner_id)
        if not task_by_id:
            return {
                       'task not found'
                   }, 400
        return {'data': task_by_id.json()}

