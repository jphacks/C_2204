import datetime
import flask_login

from database import db
from werkzeug.security import generate_password_hash, check_password_hash


class Users(flask_login.UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(225), nullable=False, primary_key=True)
    user_name = db.Column(db.String(225), nullable=False)  # 表示名

    def __init__(self, user_id: str, user_name: str):
        self.id = user_id
        self.user_name = user_name

    def get_user(user_id: str):
        return db.session.query(Users).filter(Users.id == user_id).one_or_none()

    def check_user_id(user_id: str) -> bool:
        user = Users.get_user(user_id=user_id)
        if user is not None:
            return True
        else:
            return False


class UserLogin(db.Model):  # passwordがリークしないため一応分割
    __tablename__ = "user_login"
    user_id = db.Column(db.String(225), nullable=False, primary_key=True)  # UsersのID
    password_hash = db.Column(db.String(225), nullable=False)  # ハッシュ化したパスワード
    last_login = db.Column(db.DateTime)  # 最終ログイン時刻

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password_hash = generate_password_hash(password)
        self.last_login = datetime.datetime.now()

    def authentication(user_id: str, password: str) -> bool:
        user = db.session.query(UserLogin).filter(UserLogin.user_id == user_id).one_or_none()

        if user is None or not check_password_hash(user.password_hash, password):
            return False
        else:
            return True


def create_user(user_id: str, user_name: str, password: str) -> bool:
    used_user_id = True if Users.query.filter_by(id=user_id).one_or_none() is not None else False
    if used_user_id:
        return False
    new_user = Users(user_id=user_id, user_name=user_name)
    new_user_login = UserLogin(user_id=user_id, password=password)
    try:
        db.session.add(new_user)
        db.session.add(new_user_login)
        db.session.commit()
    except Exception:
        return False
    return True
