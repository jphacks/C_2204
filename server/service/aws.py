import boto3
import uuid
import settings as s


from flask import make_response, jsonify


def get_presigned_url(folder: str):
    # TODO:確率は低いが既に使われているファイル名か確認する必要あり
    key = f"{uuid.uuid4()}.png"
    url = boto3.client(
        "s3", aws_access_key_id=s.AWS_ACCESS_KEY_ID, aws_secret_access_key=s.AWS_SECRET_ACCESS_KEY
    ).generate_presigned_url(
        ClientMethod="put_object",
        Params={"Bucket": s.AWS_S3_BUCKET_NAME, "Key": f"{folder}/{key}"},
        ExpiresIn=60,
        HttpMethod="PUT",
    )
    return make_response(jsonify(key=key, url=url))


# TODO:S3にアップロードする処理
def upload_photo(img):
    return True
