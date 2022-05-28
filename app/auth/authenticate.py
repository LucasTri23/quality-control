from functools import wraps
import jwt
from flask import request, jsonify, current_app

from app.models.user import User


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({"error": "You don't have permission to access this route."}), 403
        if not "Bearer" in token:
            return jsonify({"error": "Invalid token!"})
        try:
            pure_token = token.replace("Bearer ", "")
            decoded = jwt.decode(pure_token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(decoded['id'])
        except:
            return jsonify({"error": "Invalid token!"})
        return f(current_user=current_user, *args, **kwargs)

    return wrapper
