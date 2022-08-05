from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/logout', methods=['POST'])
def logout():
    return '<p>Logout</p>'


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = request.form.get('user')
        firstname = request.form.get('first')
        lastname = request.form.get('last')
        email = request.form.get('email')
        password = request.form.get('pass')
        print(user, firstname, lastname, email, password)

    return render_template('signup.html')
