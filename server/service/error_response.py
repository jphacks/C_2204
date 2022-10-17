from flask import make_response, jsonify


def bad_request_response():
    return make_response(jsonify({"code": 400, "status": "Bad Request"})), 400
