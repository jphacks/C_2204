import settings


def setup_db(app):
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/\
        {settings.MYSQL_DATABASE}?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
