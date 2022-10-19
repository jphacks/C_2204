import flask_login
import service
import settings as s

from flask import make_response, jsonify
from model import NbgPhotos


def __to_json(photo: NbgPhotos):
    return dict(
        {
            "key": photo.photo_key,
            "url": f"https://{s.AWS_S3_BUCKET_NAME}.s3.ap-northeast-1.amazonaws.com/nbg_img/{photo.photo_key}",
            "created_user": photo.created_user,
        }
    )


def get_photos():
    photos = NbgPhotos.get_all()
    photos_json = list(map(__to_json, photos))
    return make_response(jsonify(photos_json))


def create_nbg_photo(photo_key: str):
    # TODO:ここに画像を切り抜く処理を書く
    success = True  # 画像作成に成功した場合

    if success:
        new_nbg_photo = NbgPhotos(photo_key=str(photo_key), created_user=str(flask_login.current_user.id))
        if new_nbg_photo.regist():
            return make_response(jsonify(__to_json(new_nbg_photo)))

    return service.internal_server_error_response()
