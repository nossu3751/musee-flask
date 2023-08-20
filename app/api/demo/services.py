import traceback
from app.extensions import redis_wrapper, db
from app.api.demo.exceptions import *
from app.models.demo.user import User
from app.models.demo.artwork import Artwork
from app.models.demo.verif_vote import VerifVote
from sqlalchemy import select, update

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
            where(VerifVote.awid == awid)
        )
        
        prices=db.session.execute(stmt).scalar()
        print(prices[0], type(prices), type([prices[0]]))
        return sum(prices)/len(prices)
    






