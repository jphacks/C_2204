from flask import Blueprint, make_response, jsonify
from controller.decorated_required import required_field

api = Blueprint("api", __name__)


# ヘルスチェック
@api.get("/helth")
@required_field(required_header={"Content-Type": "application/json"})
def helth():
    return make_response(jsonify({"code": 200, "status": "ok"}))


# 作成された画像一覧
@api.get("/photos")
def get_photos():
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


# 投稿作成
@api.post("/photos")
def post_photos():
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
        return make_response(jsonify({"code": 500, "status": "Internal Server Error"})), 500


# 切り抜かれた人画像一覧
@api.get("/photos/persons")
def get_photos_persons():
    return make_response(
        jsonify([{"key": "key-name", "url": "https://my-bucket.s3-ap-northeast-1.amazonaws.com/key-name?hoge=fuga"}])
    )


# 画像から人を切り抜いてURLを返す
@api.post("/photos/crop")
def post_photos_crop():
    post_ok = False
    if post_ok:
        return make_response(jsonify(code=200))
    else:
        return make_response(jsonify({"code": 500, "status": "Internal Server Error"})), 500


# s3へのアップロード用署名付きURL
@api.get("/photos/presigned-url")
def get_photos_presigned_url():
    return make_response(
        jsonify(code=200, key="key-name", url="https://my-bucket.s3-ap-northeast-1.amazonaws.com/key-name?hoge=fuga")
    )
