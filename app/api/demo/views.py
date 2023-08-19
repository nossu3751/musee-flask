from flask import Blueprint, jsonify, request, abort
from app.api.demo.services import DemoService
from app.api.demo.utils import *
from app.models.demo.user import User
from app.models.demo.artwork import Artwork
from app.models.demo.verif_vote import VerifVote

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




