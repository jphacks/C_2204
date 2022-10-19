import datetime

from database import db


class NbgImg(db.Model):  # Non-background Image
    __tablename__ = "nbg_img"
    img_key = db.Column(db.String(225), nullable=False, primary_key=True)  # S3の保存先
    created_user = db.Column(db.String(225), nullable=False)  # UsersのID
    created_at = db.Column(db.DateTime)  # 背景を削除した日時

    def __init__(self, img_key, created_user):
        self.img_key = img_key
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
        return db.session.query(NbgImg).all()
