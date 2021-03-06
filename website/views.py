from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


# TODO - Prolly it'll be removed buddy
@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
