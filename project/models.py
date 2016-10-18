from flask_sqlalchemy import SQLAlchemy
from project import db

class Writeups(db.Model):
	__tablename__ = 'writeups'
	idwriteup = db.Column(db.Integer, primary_key = True)
	event = db.Column(db.String(100))
	task = db.Column(db.String(100))
	tags = db.Column(db.String(100))
	author = db.Column(db.String(100))
	writeup = db.Column(db.String(100))

	def __init__(self, event = "", task = "", tags = "", author = "", writeup = ""):
		self.event = event
		self.task = task
		self.tags = tags
		self.author = author
		self.writeup = writeup
