from flask_restful import Resource, reqparse
from models.task import TASKMODEL
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity


class update_delete_get_id(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'completed',
        type=bool,
        required=True
    )

    @jwt_required()
    def get(self, task_id):
        verify_jwt_in_request()
        owner_id = get_jwt_identity()
        task_by_id = TASKMODEL.get_task_to_id(task_id, owner_id)
        if not task_by_id:
            return {
                       'result': 'task not found'
                   }, 400
        return {
            'success': True,
            'data': task_by_id.json()
        }

    @jwt_required()
    def put(self, task_id):
        verify_jwt_in_request()
        owner_id = get_jwt_identity()

        data = self.parser.parse_args()
        update_task = TASKMODEL.get_task_to_id(task_id, owner_id)
        if not update_task:
            return {
                       'task not found'
                   }, 400
        update_task.completed = data['completed']
        update_task.save_to_db()
        return {'success': True,
                'data': update_task.json()
                }

    @jwt_required()
    def delete(self, task_id):
        verify_jwt_in_request()
        owner_id = get_jwt_identity()

        delete_task = TASKMODEL.get_task_to_id(task_id, owner_id)
        if not delete_task:
            return {
                'success': False,
                'massage': 'task not found'
            }, 400
        delete_task.delete_to_db()
        return {
                   'success': True
               }, 200
