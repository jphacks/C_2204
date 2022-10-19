import flask_login
import service

from flask import make_response, jsonify
from model import Users, UserLogin, create_user


def check(user_id: str):
    return make_response(jsonify({"exist": Users.check_user_id(user_id=user_id)}))


def signup(user_id, user_name, password_hash):
    success = create_user(user_id=str(user_id), user_name=str(user_name), password_hash=str(password_hash))
    if success:
        return service.created_response()
    else:
        return service.internal_server_error_response()


def signin(user_id, password_hash):
    success = UserLogin.authentication(str(user_id), str(password_hash))
    if success:
        user = Users.get_user(user_id=str(user_id))
        flask_login.login_user(user)
        return service.ok_response()
    else:
        return service.unauthorized_response()


def signout():
    flask_login.logout_user()
    return service.ok_response()
