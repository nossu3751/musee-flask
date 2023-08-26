import random
import sys
from datetime import datetime as dt, timedelta
sys.path.append(f'{sys.path[0]}/../..')

import json, traceback
from app import create_app
from app.extensions import db
from app.models.demo.user import User
from app.models.demo.artwork import Artwork
from app.models.demo.verif_vote import VerifVote
from app.api.demo.services import DemoService

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
    VerifVote.query.delete()
    Artwork.query.delete()
    User.query.delete()
    
    
    db.session.commit()

def add_user(id, email, first_name, last_name):
    try:
        user = User(id=id, email=email, first_name=first_name, last_name=last_name)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()

def add_artwork(id, uid, verified, actual_price, name, img_link, verified_dt):
    try:
        artwork = Artwork(id=id, uid=uid, verified=verified, actual_price=actual_price, name=name, img_link=img_link, verified_dt=verified_dt)
        db.session.add(artwork)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()

def add_verif_vote(uid, awid, worth, worth_price, voted_dt):
    try:
        verif_vote = VerifVote(uid=uid, awid=awid, worth=worth, worth_price=worth_price, voted_dt=voted_dt)
        db.session.add(verif_vote)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()

def main():
    seed_data = {}
    print(sys.path[0])
    with open("scripts/demo/seed_data.json") as f:
        seed_data = json.load(f)
    try:
        app = create_app()
        with app.app_context():
            db.create_all()
            delete_all()
            users = seed_data["users"]
            artworks = seed_data["artworks"]
            verif_votes = seed_data["verif_votes"]
            # user creation
            for i in range(len(users)):
                user = users[i]
                add_user(id=i+1,email=user["email"], first_name=user["first_name"], last_name=user["last_name"])
            # artwork creation
            for i in range(len(artworks)):
                artwork = artworks[i]
                verified = artwork["verified"]
                verified_dt = dt.now() -  timedelta(30) if verified else None
                add_artwork(id=i+1, uid=artwork["uid"], verified=verified, actual_price=artwork["actual_price"], name=artwork["name"], img_link=artwork["img_link"], verified_dt=verified_dt)
            
            # verif_vote creation
            date_format = "%Y/%m/%d/ %H:%M:%S.%f"
            u_aw_combinations = []
            for aw in range(1,101):
                for uid in range(1,25):
                    u_aw_combinations.append((uid,aw, True))
                for uid in range(25,100):
                    u_aw_combinations.append((uid,aw, False))

            for u_aw_combination in u_aw_combinations:
                voted_dt = dt.now()
                uid,awid,worth = u_aw_combination[0],u_aw_combination[1], u_aw_combination[2]
                worth_price = None if worth == False else random.randint(10,2000)
                add_verif_vote(uid=uid, awid = awid, worth = worth, worth_price = worth_price, voted_dt = voted_dt)
                DemoService.increment_user_token(uid)
                
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    main()