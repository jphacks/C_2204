from flask import Blueprint, make_response, jsonify

api = Blueprint("api", __name__)


# ヘルスチェック
@api.get("/helth")
def helth():
    return make_response(jsonify(code=200, status="ok"))


# 作成された画像一覧
@api.get("/photos")
def get_photos():
    return make_response(jsonify(code=200))


# 投稿作成
@api.post("/photos")
def post_photos():
    post_ok = False
    if post_ok:
        return make_response(jsonify(code=200))
    else:
        return make_response(jsonify(code=500)), 500


# s3へのアップロード用署名付きURL
@api.get("/photos/presigned-url")
def get_photos_presigned_url():
    return make_response(
        jsonify(code=200, key="key-name", url="https://my-bucket.s3-ap-northeast-1.amazonaws.com/key-name?hoge=fuga")
    )


# 切り抜かれた人画像一覧
@api.get("/photos/persons")
def get_photos_persons():
    return make_response(
        jsonify(code=200, key="key-name", url="https://my-bucket.s3-ap-northeast-1.amazonaws.com/key-name?hoge=fuga")
    )


# 画像から人を切り抜いてURLを返す
@api.post("/photos/crop")
def post_photos_crop():
    post_ok = False
    if post_ok:
        return make_response(jsonify(code=200))
    else:
        return make_response(jsonify(code=500)), 500
