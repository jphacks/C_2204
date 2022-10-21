import service
import settings as s

from flask import make_response, jsonify
from model import Posts, PostLikes, Users


def __to_json(post: Posts):
    return dict(
        {
            "photo": {
                "key": post.post_key,
                "url": f"https://{s.AWS_S3_BUCKET_NAME}.s3.ap-northeast-1.amazonaws.com/post_img/{post.post_key}",
            },
            "user": {"id": post.created_user, "name": Users.get_user(user_id=post.created_user).user_name},
            "body": post.body,
            "created_at": post.created_at,
            "likes": post.likes,
            "already_like": "",
        }
    )


def get_posts():
    posts = Posts.get_all()
    posts_json = list(map(__to_json, posts))
    return make_response(jsonify(posts_json))


def post_posts(post_key: str, body: str):
    new_post = Posts(post_key=post_key, body=body, created_user="dev")
    if new_post.regist():
        return make_response(jsonify(__to_json(new_post)))
    return service.internal_server_error_response()


def change_like(post_key: str, like: bool):
    success = PostLikes.change_like(post_key=post_key, user_id="dev", like=like)
    if success:
        return service.ok_response()
    else:
        return service.internal_server_error_response()
