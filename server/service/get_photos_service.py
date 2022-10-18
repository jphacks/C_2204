from flask import make_response, jsonify


def get_photos_response():
    return make_response(
        jsonify(
            {
                "image": {
                    "key": "key-name",
                    "url": "https://my-bucket.s3-ap-northeast-1.amazonaws.com/key-name?hoge=fuga",
                },
                "user": {},
                "body": "友達と夢の国行ってきた",
                "created_at": "2022-10-17T06:31:43.101Z",
                "likes": 0,
            }
        )
    )
