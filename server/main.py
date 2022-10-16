from flask import Flask
from database import setup_db


def setup_app():
    app = Flask(__name__)
    setup_db(app)


if __name__ == "__main__":
    setup_app()
