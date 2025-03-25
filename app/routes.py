from flask import Blueprint, render_template, abort
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@main.route('/uid/<int:uid_number>/')
def user_detail(uid_number):
    user = User.query.get_or_404(uid_number)
    return render_template('user_detail.html', user=user)
