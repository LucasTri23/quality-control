from flask import request, jsonify, Blueprint
from app import db, jwt
from sqlalchemy import exc
from app.models.user import User
from app.models.user_schema import UserSchema
from app.models.revoked_token import RevokedToken
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, \
    jwt_required, get_jwt, set_access_cookies, set_refresh_cookies, unset_jwt_cookies

user_schema = UserSchema(exclude=('employee', 'id_employee'))  # Importing User Schema to convert the data


class AuthController:
    auth_controller = Blueprint(name='auth_controller', import_name=__name__)

    # Loadind the jwt identity value
    @jwt.user_identity_loader
    def user_identity_lookup(login):
        return login

    # Checking if the token in blacklist
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_data):
        jti = jwt_data['jti']
        rt = RevokedToken.query.filter_by(jti=jti).first()
        return bool(rt)

    @auth_controller.route("/register", methods=['POST'])
    def register():
        # implement logic to check if login already exists on database
        # user = User.query.filter_by(login=login).first()

        data = request.get_json()
        user_schema = UserSchema()
        user = user_schema.load(data)

        result = user_schema.dump(user.create())
        return (jsonify({
            "user": result
        }), 201)

    @auth_controller.route('/login', methods=['POST'])
    def login():
        user = User.query.filter_by(login=request.json['login']).first_or_404()
        if user.verify_password(request.json['password']) and user.user_role == 1:
            user = user_schema.dump(user)
            # Creating access tokens
            access_token = create_access_token(user)
            refresh_token = create_refresh_token(user)
            response = jsonify({
                "access_token": access_token,
                "refresh_token": refresh_token,
            })
            # Adding tokens to response
            #set_access_cookies(response, access_token)
            #set_refresh_cookies(response, refresh_token)

            return response, 200
        else:
            response = jsonify({
                "message": "Wrong Email or Password"
            })
            return response, 401

    @auth_controller.route('/refresh', methods=['POST'])
    @jwt_required(refresh=True)
    def refresh():
        current_user = get_jwt_identity()
        access_token = create_access_token(current_user)
        response = jsonify({
            'access_token': access_token
        })
        set_access_cookies(response, access_token)
        return response, 200

    @auth_controller.route('/logout', methods=['DELETE'])
    @jwt_required()
    def logout():
        jti = get_jwt()['jti']
        try:
            rt = RevokedToken(jti=jti)
            db.session.add(rt)
            db.session.commit()
            response = jsonify({
                'message': "Succesfully logged out"
            })
            #unset_jwt_cookies(response)

            return response, 200
        except exc.IntegrityError:
            response = jsonify({
                'message': 'Database Error'
            })

            return response, 409

    # only accepts refresh tokens
    @auth_controller.route('/logout2', methods=['DELETE'])
    @jwt_required(refresh=True)
    def logout2():
        jti = get_jwt()['jti']
        try:
            rt = RevokedToken(jti=jti)
            db.session.add(rt)
            db.session.commit()
            response = jsonify({
                'message': "succesfully logged out"
            })
            #unset_jwt_cookies(response)

            return response, 200

        except exc.IntegrityError:
            response = jsonify({
                'message': 'Database Error'
            })

            return response, 409
