from flask import Blueprint, jsonify, request, abort
from app.api.demo.services import DemoService
from app.api.demo.utils import *
from app.models.demo.user import User
from app.models.demo.artwork import Artwork
from app.models.demo.verif_vote import VerifVote
import traceback

demo_blueprint = Blueprint('demo', __name__, url_prefix='/api/demo')

@demo_blueprint.route("/users/", methods=["GET"])
def get_users():
    users = DemoService.get_users()
    return jsonify([user.to_dict() for user in users])

@demo_blueprint.route("/artworks/", methods=["GET"])
def get_artworks():
    artworks = DemoService.get_artworks()
    return jsonify([artwork.to_dict() for artwork in artworks])

@demo_blueprint.route("/verif_votes/", methods=["GET"])
def get_verif_votes():
    verif_votes = DemoService.get_verif_votes()
    return jsonify([verif_vote.to_dict() for verif_vote in verif_votes])

@demo_blueprint.route("artworks/<aw>/get_avg_price/", methods=["GET"])
def get_avg_price(aw):
    try:
        price = DemoService.get_avg_price(aw)
        return jsonify(price), 200
    except Exception:
        return jsonify(traceback.format_exc())
    

@demo_blueprint.route("artworks/<aw>/get_worth_prices/", methods=["GET"])
def get_worth_prices(aw):
    try:
        prices = DemoService.get_worth_prices(aw)
        return jsonify(prices), 200
    except Exception:
        return jsonify(traceback.format_exc())



