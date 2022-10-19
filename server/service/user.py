import service

from flask import make_response, jsonify
from model import Users, create_user


def check(user_id: str):
    return make_response(jsonify({"exist": Users.check_user_id(user_id=user_id)}))


def signup(user_id, user_name, password_hash):
    success = create_user(user_id=user_id, user_name=user_name, password_hash=password_hash)
    if success:
        return service.ok_response()
    else:
        return service.internal_server_error_response()
