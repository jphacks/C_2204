import service

from flask import request
from functools import wraps


def required_field(required_header: dict = {}, required_body: dict = {}):
    """クライアントアクセス時のヘッダーに必須情報が含まれているか精査
    引数のdict型のvalueを"any"にすれば,valueの確認を行わない

    Args:
        required_header (dict, optional): _description_. Defaults to {}.
        required_body (dict, optional): _description_. Defaults to {}.
    """

    def required_field_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # ヘッダーに必須フィールドが存在するか確認
            for k, v in required_header.items():
                rh = request.headers.get(k)
                if rh is None or (v != "any" and rh != v):
                    return service.bad_request_response(f"header {k}")

            # ボディに必須フィールドが存在するか確認
            if any(required_body):
                # コンテンツタイプがapplication/jsonでない場合エラー
                if request.headers.get("Content-Type") == "application/json":
                    for k, v in required_body.items():
                        rh = request.form.get(k)
                        if rh is None or (v != "any" and rh != v):
                            return service.bad_request_response(f"body {k}")

                else:
                    return service.bad_request_response("header Content-Type")

            return func(*args, **kwargs)

        return wrapper

    return required_field_wrapper
