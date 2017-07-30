from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Settings(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    iso = db.Column(db.Integer)

    def __init__(self, iso):
        self.iso = iso
