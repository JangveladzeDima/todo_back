from flask import Flask
from flask_restful import Api

app = Flask(__name__)

api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=9999)
