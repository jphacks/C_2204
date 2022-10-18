from flask import make_response, jsonify


def get_photos_persons_response():
    return make_response(
        jsonify([{"key": "key-name", "url": "https://my-bucket.s3-ap-northeast-1.amazonaws.com/key-name?hoge=fuga"}])
    )
