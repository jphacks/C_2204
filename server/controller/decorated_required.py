from flask import request, make_response, jsonify
from functools import wraps


def required_field(required: list):
    def required_field_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for r in required:
                v = request.headers.get(r)
                if not v:
                    return make_response(jsonify({"code": 400, "status": "Bad Request"})), 400

            return func(*args, **kwargs)

        return wrapper

    return required_field_wrapper
