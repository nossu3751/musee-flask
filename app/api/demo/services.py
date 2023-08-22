import traceback
from app.extensions import redis_wrapper, db
from app.api.demo.exceptions import *
from app.models.demo.user import User
from app.models.demo.artwork import Artwork
from app.models.demo.verif_vote import VerifVote
from sqlalchemy import and_, func, select, update
import statistics

class DemoService:
    @staticmethod
    def get_users():
        stmt = select(User).order_by(User.id.asc())
        return db.session.execute(stmt).scalars()
    
    @staticmethod
    def get_artworks():
        stmt = select(Artwork).order_by(Artwork.uploaded_dt.asc())
        return db.session.execute(stmt).scalars()
    
    @staticmethod
    def get_voted_artworks(uid):
        voted_awids = db.session.query(VerifVote.awid).filter(VerifVote.uid == uid).all()
        voted_awids = [item[0] for item in voted_awids]
        return voted_awids
    
    @staticmethod
    def get_random_artworks(uid, count:int = 5):
        try:
            if count == None:
                count = 5
            else: 
                count = int(count)
        except Exception:
            count = 5
        random_artworks = db.session.query(Artwork).filter(
            Artwork.verified == False,
            Artwork.id.notin_(DemoService.get_voted_artworks(uid))
        ).order_by(func.random()).limit(count)
        return random_artworks
    
    @staticmethod
    def get_verif_votes():
        stmt = select(VerifVote).order_by(VerifVote.voted_dt.asc())
        return db.session.execute(stmt).scalars()
    
    @staticmethod
    def get_user(id):
        stmt = select(User).where(User.id == id)
        return db.session.execute(stmt).scalar_one_or_none()
    
    @staticmethod
    def increment_user_token(id, amount = 1):
        stmt = (
            update(User).
            where(User.id == id).
            values(tokens=User.tokens + amount)
        )
        db.session.execute(stmt)
        db.session.commit()

    @staticmethod
    def decrement_user_token(id, amount = 1):
        stmt = (
            update(User).
            where(User.id == id).
            values(tokens=User.tokens - amount)
        )
        db.session.execute(stmt)
        db.session.commit()

    @staticmethod
    def update_aw_verif_state(id, state):
        stmt = (
            update(Artwork).
            where(Artwork.id == id).
            values(verified = state)
        )
        db.session.execute(stmt)
        db.session.commit()

    
    @staticmethod
    def get_avg_price(awid):
        #todo: need to take care of edge care where user skips the worth price inputting
        stmt = (
            select(VerifVote.worth_price).
            where((VerifVote.awid == awid) & (VerifVote.worth_price != None))
            # where((VerifVote.awid == awid))
        )
        
        prices=db.session.execute(stmt).scalars()
        # print(prices[0], type(prices), type([prices[0]]))
        return statistics.mean(prices)
    
    @staticmethod
    def get_worth_prices(awid):
        #todo: need to take care of edge care where user skips the worth price inputting
        stmt = (
            select(VerifVote.worth_price).
            where((VerifVote.awid == awid) & (VerifVote.worth_price != None))
            # where((VerifVote.awid == awid))
        )
        
        prices=db.session.execute(stmt).scalars().all()
        # print(prices[0], type(prices), type([prices[0]]))
        return prices
    






