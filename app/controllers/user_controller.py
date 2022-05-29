from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required
from marshmallow import EXCLUDE

from app.models.user import User
from app.models.user_schema import UserSchema


class UserController:
    user_controller = Blueprint(name='user_controller', import_name=__name__)

    @user_controller.route('/users', methods=['GET'])
    @jwt_required()
    def index():
        user_list = User.query.all()
        user_schema = UserSchema(many=True)
        users = user_schema.dump(user_list)
        return (jsonify({
            "users": users
        }), 200)

    @user_controller.route('/users/<id>', methods=['GET'])
    @jwt_required()
    def get_user(id):
        user = User.query.filter_by(id_user=id).first_or_404()
        user_schema = UserSchema()
        user_dumped = user_schema.dump(user)
        return make_response(jsonify({
            "user": user_dumped
        }))
