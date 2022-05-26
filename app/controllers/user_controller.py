from flask import Blueprint, jsonify, make_response, request
from marshmallow import EXCLUDE

from app.models.user import User
from app.models.user_schema import UserSchema


class UserController:
    user_controller = Blueprint(name='user_controller', import_name=__name__)

    @user_controller.route('/users', methods=['GET'])
    def index():
        user_list = User.query.all()
        user_schema = UserSchema(unknown=EXCLUDE, many=True, exclude=['password'])
        users = user_schema.dump(user_list)
        return make_response(jsonify({
            "users": users
        }))

    @user_controller.route('/users/<id>', methods=['GET'])
    def get_user(id):
        user = User.query.get(id)
        user_schema = UserSchema()
        userDumped = user_schema.dump(user)
        return make_response(jsonify({
            "user": userDumped
        }))

    @user_controller.route('/users', methods=['POST'])
    def register():
        data = request.get_json()
        user_schema = UserSchema(unknown=EXCLUDE)
        user = user_schema.load(data)

        result = user_schema.dump(user.create())
        return make_response(jsonify({
            "user": result
        }), 201)
