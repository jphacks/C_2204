import datetime

from database import db


class NbgPhotos(db.Model):  # Non-background Image
    __tablename__ = "nbg_photos"
    photo_key = db.Column(db.String(225), nullable=False, primary_key=True)  # S3の保存先
    share = db.Column(db.Boolean, nullable=False, default=False)  # 背景を切り取った画像を共有していいか否か
    created_user = db.Column(db.String(225), nullable=False)  # UsersのID
    created_at = db.Column(db.DateTime)  # 背景を削除した日時

    def __init__(self, photo_key, share, created_user):
        self.photo_key = photo_key
        self.share = share
        self.created_user = created_user
        self.created_at = datetime.datetime.now()

    def regist(self) -> bool:
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            return False
        return True

    def get_all() -> list:
        return db.session.query(NbgPhotos).filter(NbgPhotos.share).all()
