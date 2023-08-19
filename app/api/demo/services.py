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
    def increment_user_token(id):
        stmt = (
            update(User).
            where(User.id == id).
            values(tokens=User.tokens + 1)
        )
        db.session.execute(stmt)
        db.session.commit()

    @staticmethod
    def decrement_user_token(id):
        stmt = (
            update(User).
            where(User.id == id).
            values(tokens=User.tokens - 1)
        )
        db.session.execute(stmt)
        db.session.commit()
   

    


