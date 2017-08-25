from flask import Flask, render_template, flash, redirect, request
from app import app
from .forms import LoginForm
from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView
from mongoengine import connect, Document, StringField, ListField, ReferenceField, IntField, DateTimeField 
import datetime

connect('wiki-cast')
admin = Admin(app, name='wiki admin', template_mode='bootstrap3')

class User(Document):
    user_name = StringField(max_length=50)
    email = StringField(required=True, max_length=50)
    userpw = StringField(max_length=50)
 
class Article(Document):
    author = StringField(max_length=30, required=True)
    title = StringField(max_length=120, required=True)
    content = StringField(required=True)
    tags = ListField(StringField(max_length=30))
    date = DateTimeField(default=datetime.datetime.now)

    
admin.add_view(ModelView(User))
admin.add_view(ModelView(Article))

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html',
                            title='Home',
                            articles=Article.objects)

@app.route('/wiki_page')
def wiki_page():
    return render_template('wiki_page.html',
                           title='Wiki page',
                           articles=Article.objects)

@app.route('/analyzer')
def analyzer():
    return render_template('analyzer.html',
                           title='analyser')

@app.route('/login', methods=['GET', 'POST'])
def login():
    _form = LoginForm()
    if _form.validate_on_submit():
        return redirect('/index')       
    return render_template('login.html',
                           title='Sign In',
                           form=_form,
                           providers=app.config['OPENID_PROVIDERS'])
    
@app.route('/process', methods=['POSt'])
def process():
    _username = request.form.get('username')
    
    if _username:
        return render_template('login_response.html',
                               title='Hello',
                               username=_username)
    else:
        return 'please go back and entre your name...', 400

