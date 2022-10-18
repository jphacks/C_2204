from database import db


class NbgImg(db.Model):
    __tablename__ = "nbgimg"
    img_path = db.Column(db.String(225), nullable=False, primary_key=True)


db.create_all()
