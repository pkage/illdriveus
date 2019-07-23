from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

bp = Blueprint('dashboard', __name__)


@bp.route('/')
def index():
    return render_template('/index.html')
