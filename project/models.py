#from flask_sqlalchemy import SQLAlchemy
from project import db


class Writeups(db.Model):
    __tablename__ = 'writeups'
    idwriteup = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(255))
    task = db.Column(db.String(255))
    tags = db.Column(db.String(255))
    author = db.Column(db.String(255))
    ctftime_link = db.Column(db.String(255))
    original_writeup = db.Column(db.String(255))

    def __init__(self, data):
        self.idwriteup = int(data['idWriteup'])
        self.event = str(data['event'])
        self.task = str(data['task'])
        self.tags = str(data['tags'])
        self.author = str(data['author']).decode('utf-8', 'ignore')
        self.ctftime_link = str(data['writeupUrl'])
        self.original_writeup = str(data['originalWriteup'])
