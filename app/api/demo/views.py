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

@demo_blueprint.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = DemoService.get_user(id)
    if not user:
        abort(404)
    return jsonify(user.to_dict()), 200

@demo_blueprint.route("/artworks/", methods=["GET"])
def get_artworks():
    uid = request.args.get("uid")
    if uid == None:   
        artworks = DemoService.get_artworks()
    else:
        artworks = DemoService.get_user(uid).artworks
    return jsonify([artwork.to_dict() for artwork in artworks])

@demo_blueprint.route("/random_artworks/",methods=["GET"])
def get_random_artworks():
    count = request.args.get("count")
    uid = request.args.get("uid")
    random_artworks = DemoService.get_random_artworks(uid, count)
    return jsonify([aw.to_dict() for aw in random_artworks])


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
        return jsonify(traceback.format_exc()), 500
    
@demo_blueprint.route("artworks/vote", methods=["PUT"])
def vote():
    try:
        res = request.json
        uid = res["uid"]
        awid = res["awid"]
        worth = res["worth"]
        voted = DemoService.vote(uid, awid, worth)
        if not voted:
            return jsonify(traceback.format_exc()), 409
        vote_count = DemoService.get_aw_verif_votes_count(awid)
        positive_count = DemoService.get_positive_verif_votes_count(awid)
        if positive_count >= 25:
            DemoService.update_aw_verif_state(awid, True)
        elif vote_count >= 100:
            DemoService.delete_artwork(awid)
        return jsonify("Success"), 200
    except Exception:
        return jsonify(traceback.format_exc()), 500

    

@demo_blueprint.route("artworks/<aw>/get_worth_prices/", methods=["GET"])
def get_worth_prices(aw):
    try:
        prices = DemoService.get_worth_prices(aw)
        return jsonify(prices), 200
    except Exception:
        return jsonify(traceback.format_exc())



