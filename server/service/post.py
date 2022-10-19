import flask_login
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
            "already_like": ""
            if not flask_login.current_user.is_authenticated
            else PostLikes.get_like(post_key=post.post_key, user_id=flask_login.current_user.id),
        }
    )


def get_posts():
    posts = Posts.get_all()
    posts_json = list(map(__to_json, posts))
    return make_response(jsonify(posts_json))
