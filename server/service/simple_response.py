from flask import make_response, jsonify


def ok_response():
    # 200 OK
    return make_response(jsonify({"code": 200, "status": "OK"}))


def created_response():
    # 201 Created
    return make_response(jsonify({"code": 201, "status": "Created"})), 201


def bad_request_response(message: str = "request"):
    # 400 Bad Request
    return make_response(jsonify({"code": 400, "status": "Bad Request", "message": f"check {str(message)}"})), 400


def unauthorized_response(message: str = "request"):
    # 401 Unauthorized
    return make_response(jsonify({"code": 401, "status": "Unauthorized"})), 401


def internal_server_error_response():
    # 500 Internal Server Error
    return make_response(jsonify({"code": 500, "status": "Internal Server Error"})), 500
