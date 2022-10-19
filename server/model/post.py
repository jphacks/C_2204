import datetime

from database import db


class Posts(db.Model):  # 投稿一覧
    __tablename__ = "posts"
    post_key = db.Column(db.String(225), nullable=False, primary_key=True)  # S3のpost用の保存先
    body = db.Column(db.String(225))  # 投稿の本文
    likes = db.Column(db.Integer, default=0)  # いいねの数 DBの負荷を減らすため投稿に保存
    created_user = db.Column(db.String(225), nullable=False)  # UsersのID
    created_at = db.Column(db.DateTime)  # 投稿日

    def __init__(self, post_key, body, created_user):
        self.post_key = post_key
        self.body = body
        self.likes = 0
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
        return db.session.query(Posts).all()


class PostLikes(db.Model):  # 誰がどの投稿にいいねをしたか管理
    __tablename__ = "post_likes"
    post_key = db.Column(db.String(225), nullable=False, primary_key=True)  # PostsのID 複合キー
    user_id = db.Column(db.String(225), nullable=False, primary_key=True)  # UsersのID 複合キー
    like = db.Column(db.Boolean, nullable=False, default=True)  # 投稿に対してユーザがいいねを押しているか

    def __init__(self, post_key, user_id, like):
        self.post_key = post_key
        self.user_id = user_id
        self.like = like

    def get_like(post_key, user_id) -> bool:
        user_like = (
            db.session.query(PostLikes)
            .filter(PostLikes.post_key == post_key, PostLikes.user_id == user_id)
            .one_or_none()
        )
        if user_like is None:
            return False
        else:
            return user_like.like

    def change_like(post_key, user_id, like) -> bool:
        user_like = (
            db.session.query(PostLikes)
            .filter(PostLikes.post_key == post_key, PostLikes.user_id == user_id)
            .one_or_none()
        )
        post = db.session.query(Posts).filter(Posts.post_key == post_key).one()
        if user_like is None:
            user_like = PostLikes(post_key=str(post_key), user_id=str(user_id), like=like)
            if like:
                post.likes += 1
            else:
                post.likes -= 1
        else:
            if not user_like.like and like:
                post.likes += 1
            elif user_like.like and not like:
                post.likes -= 1
            user_like.like = like

        try:
            db.session.add(user_like)
            db.session.add(post)
            db.session.commit()
        except Exception:
            return False
        return True
