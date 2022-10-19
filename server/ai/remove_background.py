import service
import io
import urllib
import settings as s

# from PIL import Image
from rembg.bg import remove


def remove_bg(photo_key: str) -> bool:
    photo_url = f"https://{s.AWS_S3_BUCKET_NAME}.s3.ap-northeast-1.amazonaws.com/up_img/{photo_key}"
    # インターネットから画像を取得する処理
    with urllib.request.urlopen(photo_url) as web_file:
        data = web_file.read()

    # 背景を削除
    result = remove(data)

    if img_check_filter(result):
        # TODO:S3にアップデートする用の処理
        if service.aws.upload_photo(img=io.BytesIO(result), key=photo_key):
            # 正常終了
            return True

    return False


def img_check_filter(result) -> bool:
    # output = Image.open(io.BytesIO(result)).convert("RGBA")
    # output.show()
    return True
