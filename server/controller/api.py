import service

from flask import Blueprint, request
from controller.decorated_required import required_field

api = Blueprint("api", __name__)


# ヘルスチェック
@api.get("/health")
def health():
    return service.ok_response()


@api.post("/user/check")
@required_field(required_header={"Content-Type": "application/json"}, required_body={"user_id": "any"})
def post_user_check():
    return service.user.check(user_id=request.form.get("user_id"))


# s3へのアップロード用署名付きURL
@api.get("/photos/presigned-url")
def get_photos_presigned_url():
    return service.get_photos_presigned_url_response()


# 作成された画像一覧
@api.get("/photos")
def get_photos():
    return service.get_photos_response()


# 投稿作成
@api.post("/photos")
@required_field(required_header={"Content-Type": "application/json"}, required_body={"key": "any", "body": "any"})
def post_photos():
    return service.post_photos_response()


# 切り抜かれた人画像一覧
@api.get("/photos/persons")
def get_photos_persons():
    return service.get_photos_persons_response()


# 画像から人を切り抜いてURLを返す
@api.post("/photos/crop")
@required_field(required_header={"Content-Type": "application/json"}, required_body={"key": "any"})
def post_photos_crop():
    return service.post_photos_crop_response()
