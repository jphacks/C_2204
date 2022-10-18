from flask import make_response, jsonify


def ok_response():
    return make_response(jsonify({"code": 200, "status": "ok"}))


def bad_request_response(message: str = "request"):
    # 400 Bad Request
    return make_response(jsonify({"code": 400, "status": "Bad Request", "message": f"check {str}"})), 400


def internal_server_error_response():
    # 500 Internal Server Error
    return make_response(jsonify({"code": 500, "status": "Internal Server Error"})), 500
