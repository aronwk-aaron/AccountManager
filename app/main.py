from flask import render_template, Blueprint, redirect, url_for, request, send_from_directory
from flask_user import login_required, current_user
import json

from app.models import Account, AccountInvitation
from app.schemas import AccountSchema

main_blueprint = Blueprint('main', __name__)

account_schema = AccountSchema()

@main_blueprint.route('/', methods=['GET'])
def index():
    """Home/Index Page"""
    if current_user.is_authenticated:
        account_data = json.loads(
            account_schema.jsonify(
                Account.query.filter(Account.id == current_user.id).first()
            ).data
        )
        del account_data["password"]
        return render_template('main/index.html.j2', account_data=account_data)
    else:
        return render_template('main/index.html.j2')

@main_blueprint.route('/about')
def about():
    """About Page"""
    return render_template('main/about.html.j2')

@main_blueprint.route('/favicon.ico')
def favicon():
    return send_from_directory(
        'static/logo/',
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )
