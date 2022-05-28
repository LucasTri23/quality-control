import datetime

import jwt
from flask import Blueprint, jsonify, make_response, request
from marshmallow import EXCLUDE

from app import app
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

    @user_controller.route('/users/login', methods=['POST'])
    def login():
        login = request.json['login']
        password = request.json['password']
        user = User.query.filter_by(login=login).first_or_404()

        if not user.verify_password(password):
            return jsonify({
                "error": "Wrong credentials!"
            }), 403

        payload = {
            "id": user.id_user,
            "login": user.login,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }
        token = jwt.encode(payload, app.config['SECRET_KEY'])
        return make_response(jsonify({
            "token": token
        }), 201)
