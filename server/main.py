import controller
import flask_login
import service
import settings as s
import waitress

from database import setup_db
from flask import Flask
from flask_cors import CORS
from model import Users


# appの設定
app = Flask(__name__)
app.secret_key = s.APP_SECRET_KEY

# ログイン管理
login_manager = flask_login.LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return service.unauthorized_response()


# DB関連の設定
setup_db(app)

# APIのルーティングをロード
app.register_blueprint(controller.api)

CORS(app, supports_credentials=True)


if __name__ == "__main__":
    # NOTE:host="0.0.0.0"は外部からアクセスする際に必須
    if s.ENVIRONMENT == "dev":
        app.run(host="0.0.0.0", debug=True, port=s.APP_PORT)
    else:
        waitress.serve(app, host="0.0.0.0", port=s.APP_PORT, threads=10)
