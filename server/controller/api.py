import flask_login
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


# signin
@api.post("/user/signin")
@required_field(
    required_header={"Content-Type": "application/json"},
    required_body={"user_id": "any", "password_hash": "any"},
)
def post_user_signin():
    request_body = request.json
    return service.user.signin(
        user_id=request_body["user_id"],
        password_hash=request_body["password_hash"],
    )


# signout
@api.get("/user/signout")
@flask_login.login_required
def get_user_signout():
    return service.user.signout()


# s3へのアップロード用署名付きURL
@api.get("/photos/presigned-url")
def get_photos_presigned_url():
    return service.aws.get_presigned_url(folder="up_img")


# 切り抜かれた人画像一覧
@api.get("/photos/persons")
def get_photos_persons():
    return service.photos.get_photos()


# 画像から人を切り抜いてURLを返す
@api.post("/photos/crop")
@flask_login.login_required
@required_field(required_header={"Content-Type": "application/json"}, required_body={"key": "any"})
def post_photos_crop():
    request_body = request.json
    return service.photos.create_nbg_photo(
        photo_key=request_body["key"],
    )


# s3へのアップロード用署名付きURL
@api.get("/post/presigned-url")
def get_post_presigned_url():
    return service.aws.get_presigned_url(folder="post_img")


# 作成された画像一覧
@api.get("/post")
def get_post():
    return service.post.get_posts()


# 投稿作成
@api.post("/post")
@flask_login.login_required
@required_field(required_header={"Content-Type": "application/json"}, required_body={"key": "any", "body": "any"})
def post_post():
    request_body = request.json
    return service.post.post_posts(post_key=request_body["key"], body=request_body["body"])


# いいねを押す/取り消す
@api.post("/post/like")
@flask_login.login_required
@required_field(required_header={"Content-Type": "application/json"}, required_body={"key": "any", "like": "any"})
def post_post_like():
    request_body = request.json
    return service.post.change_like(post_key=request_body["key"], like=request_body["like"])
