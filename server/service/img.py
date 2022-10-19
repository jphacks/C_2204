import boto3
import flask_login
import service
import settings as s
import uuid

from flask import make_response, jsonify
from model import NbgImg


def get_presigned_url():
    # TODO:確率は低いが既に使われているファイル名か確認する必要あり
    key = f"{uuid.uuid4()}.png"
    url = boto3.client(
        "s3", aws_access_key_id=s.AWS_ACCESS_KEY_ID, aws_secret_access_key=s.AWS_SECRET_ACCESS_KEY
    ).generate_presigned_url(
        ClientMethod="put_object",
        Params={"Bucket": s.AWS_S3_BUCKET_NAME, "Key": f"up_img/{key}"},
        ExpiresIn=60,
        HttpMethod="PUT",
    )
    return make_response(jsonify(key=key, url=url))


def __to_json(img_info: NbgImg):
    return dict(
        {
            "key": img_info.img_key,
            "url": f"https://{s.AWS_S3_BUCKET_NAME}.s3.ap-northeast-1.amazonaws.com/nbg_img/{img_info.img_key}",
            "created_user": img_info.created_user,
        }
    )


def get_persons():
    persons_img = NbgImg.get_all()
    persons_json = list(map(__to_json, persons_img))
    return make_response(jsonify(persons_json))


def create_nbg_img(img_key: str):
    # TODO:ここに画像を切り抜く処理を書く
    success = True  # 画像作成に成功した場合

    if success:
        new_nbg_img = NbgImg(img_key=str(img_key), created_user=str(flask_login.current_user.id))
        if new_nbg_img.regist():
            return make_response(jsonify(__to_json(new_nbg_img)))

    return service.internal_server_error_response()
