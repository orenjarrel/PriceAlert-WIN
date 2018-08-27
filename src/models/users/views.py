from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
from src.models.users.user import User

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        #  Check login is valid
        email = request.form['email']
        password = request.form['hashed']

        if User.is_login_valid(email, password):
            session['email'] = email
            # url_for gets the URL for a specific method()
            return redirect(url_for(".user_alerts"))

    return render_template("users/login.html")


@user_blueprint.route('/register')
def register_user():
    pass


@user_blueprint.route('/alerts')
def user_alerts():
    return "This is the alerts page."


@user_blueprint.route('/logout')
def logout_user():
    pass


@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts():
    pass
