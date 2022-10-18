import uuid

from database import db


class Photos(db.Model):  # 投稿一覧
    __tablename__ = "photos"
    id = db.Column(db.String(225), nullable=False, primary_key=True)  # uuid
    created_user = db.Column(db.String(225), nullable=False)  # UsersのID
    body = db.Column(db.String(225))  # 投稿の本文
    likes = db.Column(db.Integer, default=0)  # いいねの数

    def __init__(self, created_user, body):
        self.id = uuid.uuid4()
        self.created_user = created_user
        self.body = body
        self.likes = 0


class PhotoLikes(db.Model):  # 誰がどの投稿にいいねをしたか管理
    __tablename__ = "photo_likes"
    photos_id = db.Column(db.String(225), nullable=False, primary_key=True)  # PhotosのID
    user_id = db.Column(db.String(225), nullable=False, primary_key=True)  # UsersのID
    like = db.Column(db.Boolean, nullable=False, default=True)  # 投稿に対してユーザがいいねを押しているか

    def __init__(self, photos_id, user_id, like):
        self.photos_id = photos_id
        self.user_id = user_id
        self.like = like


db.create_all()
