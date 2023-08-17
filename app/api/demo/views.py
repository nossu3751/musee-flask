from flask import Blueprint, jsonify, request, abort
from app.api.demo.services import DemoService
from app.api.demo.utils import *

demo_blueprint = Blueprint('demo', __name__, url_prefix='/api/demo')

@demo_blueprint.route("/users/", methods=["GET"])
def get_users():
    ...