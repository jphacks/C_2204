import boto3
import settings as s
import uuid

from flask import make_response, jsonify


def get_photos_presigned_url_response():
    key = f"up_img/{uuid.uuid4()}.png"
    url = boto3.client(
        "s3", aws_access_key_id=s.AWS_ACCESS_KEY_ID, aws_secret_access_key=s.AWS_SECRET_ACCESS_KEY
    ).generate_presigned_url(
        ClientMethod="put_object",
        Params={"Bucket": s.AWS_S3_BUCKET_NAME, "Key": key},
        ExpiresIn=60,
        HttpMethod="PUT",
    )
    return make_response(jsonify(key=key, url=url))
