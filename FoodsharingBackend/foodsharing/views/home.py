from flask import Blueprint

home = Blueprint('home', __name__)

@home.route('/')
def hello():
    return '<H1>Hello, World!<H1>'