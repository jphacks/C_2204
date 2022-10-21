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
@api.get("/users/check")
@required_field()
def post_user_check():
    user_id = request.args.get("user-id")
    if user_id is None:
        return service.bad_request_response()
    return service.user.check(user_id=user_id)


# 新規にユーザを作成
@api.post("/users/signup")
@required_field(
    required_header={"Content-Type": "application/json"},
    required_body={"user_id": "any", "user_name": "any", "password": "any"},
)
def post_user_signup():
    request_body = request.json
    return service.user.signup(
        user_id=request_body["user_id"],
        user_name=request_body["user_name"],
        password=request_body["password"],
    )


# signin
@api.post("/users/signin")
@required_field(
    required_header={"Content-Type": "application/json"},
    required_body={"user_id": "any", "password": "any"},
)
def post_user_signin():
    request_body = request.json
    return service.user.signin(
        user_id=request_body["user_id"],
        password=request_body["password"],
    )


# signout
@api.get("/users/signout")
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
@required_field(required_header={"Content-Type": "application/json"}, required_body={"key": "any"})
def post_photos_crop():
    request_body = request.json
    share = False
    if "share" in request_body:
        share = request_body["share"]
    return service.photos.create_nbg_photo(
        photo_key=request_body["key"],
        share=share,
    )


# s3へのアップロード用署名付きURL
@api.get("/posts/presigned-url")
def get_post_presigned_url():
    return service.aws.get_presigned_url(folder="post_img")


# 作成された画像一覧
@api.get("/posts")
def get_post():
    return service.post.get_posts()


# 投稿作成
@api.post("/posts")
@required_field(required_header={"Content-Type": "application/json"}, required_body={"key": "any", "body": "any"})
def post_post():
    request_body = request.json
    return service.post.post_posts(post_key=request_body["key"], body=request_body["body"])


# いいねを押す
@api.post("/posts/<string:post_id>/like")
@flask_login.login_required
def post_post_like(post_id):
    return service.post.change_like(post_key=post_id, like=True)


# いいねを取り消す
@api.delete("/posts/<string:post_id>/like")
@flask_login.login_required
def delete_post_like(post_id):
    return service.post.change_like(post_key=post_id, like=False)


# ヘッダー情報を追加
@api.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response
