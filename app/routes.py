from flask import Blueprint, render_template
routes_blueprint = Blueprint('routes_blueprint', __name__)


@routes_blueprint.route('/')
def index():
    return render_template('index.html')
