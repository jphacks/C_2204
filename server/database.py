from flask_sqlalchemy import SQLAlchemy
import settings as s

db = SQLAlchemy()


def setup_db(app):
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql://{s.MYSQL_USER}:{s.MYSQL_PASSWORD}@{s.MYSQL_HOST}:{s.MYSQL_PORT}/{s.MYSQL_DATABASE}?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
