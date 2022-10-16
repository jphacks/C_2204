from flask import Flask
from database import setup_db

import routing
import settings as s

DEBUG = False


def setup_app():
    app = Flask(__name__)
    app.secret_key = s.APP_SECRET_KEY
    setup_db(app)

    app.register_blueprint(routing.api)
    return app


if __name__ == "__main__":
    app = setup_app()
    app.run(host="0.0.0.0", debug=DEBUG, port=s.APP_PORT)
