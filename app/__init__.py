from flask import Flask
from app.config import config
from .api import api

from .pages import *


app = Flask(__name__)


@app.get('/')
def index():
    return Index(config, api).render()


@app.get('/login')
def login():
    return Login(config, api).render()


@app.post('/login')
def post_login():
    return PostLogin(config, api).render()
