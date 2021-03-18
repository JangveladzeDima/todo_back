from flask_restful import Resource, reqparse
from models.task import TASKMODEL
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity


class new_task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'description',
        type=str,
        required=True,
    )

    @jwt_required()
    def post(self):
        verify_jwt_in_request()
        _id = get_jwt_identity()
        data = self.parser.parse_args()

        new_task = TASKMODEL(data['description'], _id)
        new_task.save_to_db()
        return new_task.json()


class all_task(Resource):
    @jwt_required()
    def get(self):
        verify_jwt_in_request()
        _id = get_jwt_identity()
        tasks = []
        counter = 0
        for i in TASKMODEL.query.filter_by(owner=_id):
            tasks.append(i.json())
            counter += 1
        return {
                   'count': counter,
                   'data': tasks
               }, 200


class update_delete_tasks(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'completed',
        type=bool,
        required=True
    )

    @jwt_required()
    def put(self, task_id):
        verify_jwt_in_request()
        owner_id = get_jwt_identity()

        data = self.parser.parse_args()
        update_task = TASKMODEL.get_task(task_id, owner_id)
        if not update_task:
            return {
                       'task not found'
                   }, 400
        update_task.completed = data['completed']
        update_task.save_to_db()
        return {'update': 'success',  'data': update_task.json()}

    @jwt_required()
    def delete(self, task_id):
        verify_jwt_in_request()
        owner_id = get_jwt_identity()

        delete_task = TASKMODEL.get_task(task_id, owner_id)
        print(delete_task)
        if not delete_task:
            return {
                'massage': 'task not found'
            }, 400
        delete_task.delete_to_db()
        return{
            'massage': 'task deleted'
        }, 200