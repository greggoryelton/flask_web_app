from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def dev_login():
    return "<p>Login</p>"

@auth.route('/logout')
def dev_logout():
    return "<p>Logout</p>"


