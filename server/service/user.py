from flask import make_response, jsonify
from model import Users


def check(user_id: str):
    if Users.check_user_id(user_id=user_id):
        return make_response(jsonify({"exist": True}))
    else:
        return make_response(jsonify({"exist": False}))
