import sys
sys.path.append(f'{sys.path[0]}/../..')

import json, traceback
from app import create_app
from app.extensions import db
from app.models.demo.user import User
from app.models.demo.artwork import Artwork
from app.models.demo.verif_vote import VerifVote

'''
class VerifVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    awid = db.Column(db.Integer, ForeignKey('artwork.id'), nullable=False)
    worth = db.Column(db.Boolean, server_default=expression.false(), nullable=False) 
    worth_price = db.Column(db.Integer, nullable=True)
    voted_dt = db.Column(db.DateTime, default=func.now())
    
    def __repr__(self):
        return f'<VerifVote {self.id}>'
'''

def delete_all():
    User.query.delete()
    Artwork.query.delete()
    VerifVote.query.delete()
    db.session.commit()

def add_user(email, first_name, last_name):
    try:
        user = User(email=email, first_name=first_name, last_name=last_name)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()

def add_artwork(uid, verified, actual_price, name, img_link):
    try:
        artwork = Artwork(uid=uid, verified=verified, actual_price=actual_price, name=name, img_link=img_link)
        db.session.add(artwork)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()

def add_vote(uid, awid, worth, worth_price):
    try:
        verif_vote = VerifVote(uid=uid, awid=awid, worth=worth, worth_price=worth_price)
        db.session.add(verif_vote)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()

def main():
    seed_data = {}
    with open("./seed_data.json") as f:
        seed_data = json.load(f)
    try:
        app = create_app()
        with app.app_context():
            db.create_all()
            delete_all()
            users = seed_data["users"]
            artworks = seed_data["artworks"]
            for user in users:
                add_user(email=user["email"], first_name=user["first_name"], last_name=user["last_name"])
            for artwork in artworks:
                add_artwork(uid=artwork["uid"], verified=artwork["verified"], actual_price=artwork["actual_price"], name=artwork["name"], img_link=artwork["img_link"])
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    main()