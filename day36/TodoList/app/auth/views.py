
from app.auth import  auth


@auth.route('/login')
def login():
    return 'login'


@auth.route('/')
def index():
    return 'index'

