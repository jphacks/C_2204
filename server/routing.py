from flask import Blueprint, make_response, jsonify

api = Blueprint("api", __name__)


@api.get("/helth")
def helth():
    return make_response(jsonify(code=200, status="ok"))
