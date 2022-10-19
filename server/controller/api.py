import service

from flask import Blueprint, request
from controller.decorated_required import required_field

api = Blueprint("api", __name__)


# ヘルスチェック
@api.get("/health")
def health():
    return service.ok_response()


# 入力されたユーザが存在しているか確認
@api.post("/user/check")
@required_field(required_header={"Content-Type": "application/json"}, required_body={"user_id": "any"})
def post_user_check():
    request_body = request.json
    return service.user.check(user_id=request_body["user_id"])


# 新規にユーザを作成
@api.post("/user/signup")
@required_field(
    required_header={"Content-Type": "application/json"},
    required_body={"user_id": "any", "user_name": "any", "password_hash": "any"},
)
def post_user_signup():
    request_body = request.json
    return service.user.signup(
        user_id=request_body["user_id"],
        user_name=request_body["user_name"],
        password_hash=request_body["password_hash"],
    )


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
