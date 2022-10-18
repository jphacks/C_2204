import service

from flask import make_response, jsonify


def post_photos_response():
    post_ok = False
    if post_ok:
        return (
            make_response(
                jsonify(
                    {
                        "image": {
                            "key": "key-name",
                            "url": "https://my-bucket.s3-ap-northeast-1.amazonaws.com/key-name?hoge=fuga",
                        },
                        "user": {},
                        "body": "友達と夢の国行ってきた",
                        "created_at": "2022-10-17T06:35:53.269Z",
                        "likes": 0,
                    }
                )
            ),
            201,
        )
    else:
        return service.internal_server_error_response()
