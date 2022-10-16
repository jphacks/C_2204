from IPython.display import Image, display_png
from rembg.bg import remove
import numpy as np
import io
from PIL import Image
import os
import boto3
import logging
from botocore.exceptions import ClientError

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

#   if endpoint_url := os.getenv('AWS_S3_ENDPOINT_URL'):
#       s3 = boto3.client("s3", endpoint_url=endpoint_url, config=Config(signature_version="s3v4"))
#   else:
#       s3 = boto3.client("s3", config=Config(signature_version="s3v4", region_name=os.getenv('AWS_S3_REGION_NAME', 'ap-northeast-1')))


# comment

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def remove_bg(image: Image, file_name='./sample.png'):

    f = np.fromfile(file_name)
    result = remove(f,
                    alpha_matting=True,
                    alpha_matting_foreground_threshold=240,
                    alpha_matting_background_threshold=10,
                    alpha_matting_erode_structure_size=6
                    )

    output = Image.open(io.BytesIO(result)).convert("RGBA")

    # save image
    upload_file(file_name, output, object_name=None)

    return output
