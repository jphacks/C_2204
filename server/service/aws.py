import boto3
import uuid
import settings as s

from botocore.client import Config
from flask import make_response, jsonify

__client = boto3.client(
    "s3",
    aws_access_key_id=s.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=s.AWS_SECRET_ACCESS_KEY,
    config=Config(signature_version="s3v4", region_name="ap-northeast-1"),
)


def get_presigned_url(folder: str):
    # TODO:確率は低いが既に使われているファイル名か確認する必要あり
    key = f"{uuid.uuid4()}.png"
    url = __client.generate_presigned_url(
        ClientMethod="put_object",
        Params={"Bucket": s.AWS_S3_BUCKET_NAME, "Key": f"{folder}/{key}"},
        ExpiresIn=60,
        HttpMethod="PUT",
    )
    return make_response(jsonify(key=key, url=url))


# S3にアップロードする処理
def upload_photo(img, key):
    try:
        __client.upload_fileobj(img, s.AWS_S3_BUCKET_NAME, f"nbg_img/{key}")
    except Exception:
        return False
    return True
