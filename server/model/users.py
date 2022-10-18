import datetime
import flask_login

from database import db


class Users(flask_login.UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(225), nullable=False, primary_key=True)
    user_name = db.Column(db.String(225), nullable=False)  # 表示名

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name


class UserLogin(db.Model):  # passwordがリークしないため一応分割
    __tablename__ = "user_login"
    user_id = db.Column(db.String(225), nullable=False, primary_key=True)  # UsersのID
    password_hash = db.Column(db.String(225), nullable=False)  # ハッシュ化したパスワード
    last_login = db.Column(db.DateTime)  # 最終ログイン時刻

    def __init__(self, user_id, password_hash):
        self.user_id = user_id
        self.password_hash = password_hash
        self.last_login = datetime.datetime.now()


db.create_all()


def create_user(user_id, user_name, password_hash) -> bool:
    used_user_id = True if Users.query.filter_by(id=user_id).one_or_none() is not None else False
    if used_user_id:
        return False
    new_user = Users(user_id=user_id, user_name=user_name)
    new_user_login = UserLogin(user_id=user_id, password_hash=password_hash)
    try:
        db.session.add(new_user)
        db.session.add(new_user_login)
        db.session.commit()
    except Exception:
        return False
    return True
