from flask_restful import Resource, reqparse
from models.task import TASKMODEL
from flask import request
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
        owner_id = get_jwt_identity()
        value = request.args.get("completed")
        limit = request.args.get("limit")
        skip = request.args.get("skip")
        tasks = []
        if limit and skip:
            limit = int(limit)
            skip = int(skip)
            cnt = 0
            cnt1 = 0
            for i in TASKMODEL.query.filter_by(owner=owner_id):
                if cnt >= skip and cnt1 < limit:
                    tasks.append(i)
                    cnt1 += 1
                cnt += 1
            return {
                'data': [x.json() for x in tasks]
            }
        if value:
            if value == 'true':
                value = bool(True)
            else:
                value = bool(False)
            task_complated = TASKMODEL.get_task_to_complated(owner_id, value)
            return {
                'data': [x.json() for x in task_complated]
            }
        counter = 0
        for i in TASKMODEL.query.filter_by(owner=owner_id):
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
        update_task = TASKMODEL.get_task_to_id(task_id, owner_id)
        if not update_task:
            return {
                       'task not found'
                   }, 400
        update_task.completed = data['completed']
        update_task.save_to_db()
        return {'update': 'success', 'data': update_task.json()}

    @jwt_required()
    def delete(self, task_id):
        verify_jwt_in_request()
        owner_id = get_jwt_identity()

        delete_task = TASKMODEL.get_task_to_id(task_id, owner_id)
        print(delete_task)
        if not delete_task:
            return {
                       'massage': 'task not found'
                   }, 400
        delete_task.delete_to_db()
        return {
                   'massage': 'task deleted'
               }, 200
