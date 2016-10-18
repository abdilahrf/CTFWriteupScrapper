from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
import os

#Flask and SQLAlchemy initialisasi
app = Flask(__name__)
app.secret_key = "TITITD_KUDA"
db = SQLAlchemy(app)

#Settingan sqlite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

#Ignore warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from project import routes,models