import settings as s


def setup_db(app):
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql://{s.MYSQL_USER}:{s.MYSQL_PASSWORD}@{s.MYSQL_HOST}:{s.MYSQL_PORT}/{s.MYSQL_DATABASE}?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
