from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView
from mongoengine import connect, Document, StringField, ListField, ReferenceField, IntField, DateTimeField 
import datetime
import os, binascii
from app.libs.mongoengine.document import EmbeddedDocument
from app.libs.mongoengine.base.fields import ObjectIdField


app = Flask(__name__)

app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))
app.config.from_object('config')
app.config['MONGODB_SETTINGS'] = {
    'db': 'wiki_database',
    'host': 'mongodb://admin:mgo@localhost/wiki_database',
    'port': 8000
    }

from .models import views


