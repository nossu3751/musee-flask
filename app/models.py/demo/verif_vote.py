from app.extensions import db
from sqlalchemy.sql import expression
from sqlalchemy import ForeignKey, func

class VerifVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    awid = db.Column(db.Integer, ForeignKey('artwork.id'), nullable=False)
    worth = db.Column(db.Boolean, server_default=expression.false(), nullable=False) 
    worth_price = db.Column(db.Integer, nullable=True)
    voted_dt = db.Column(db.DateTime, default=func.now())
    
    def __repr__(self):
        return f'<VerifVote {self.id}>'
    