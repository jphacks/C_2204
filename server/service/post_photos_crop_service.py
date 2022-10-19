import service

from flask import make_response, jsonify


def post_photos_crop_response():
    post_ok = False
    if post_ok:
        return make_response(jsonify(code=200))
    else:
        return service.internal_server_error_response()
