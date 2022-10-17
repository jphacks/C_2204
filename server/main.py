from flask import Flask
from database import setup_db

import controller
import settings as s

DEBUG = True


def create_app():
    # appの設定
    app = Flask(__name__)
    app.secret_key = s.APP_SECRET_KEY

    # DB関連の設定
    setup_db(app)

    # APIのルーティングをロード
    app.register_blueprint(controller.api)

    return app


if __name__ == "__main__":
    app = create_app()
    # NOTE:host="0.0.0.0"は外部からアクセスする際に必須
    app.run(host="0.0.0.0", debug=DEBUG, port=s.APP_PORT)
