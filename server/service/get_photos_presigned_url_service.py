from flask import make_response, jsonify


def get_photos_presigned_url_response():
    return make_response(
        jsonify(code=200, key="key-name", url="https://my-bucket.s3-ap-northeast-1.amazonaws.com/key-name?hoge=fuga")
    )
