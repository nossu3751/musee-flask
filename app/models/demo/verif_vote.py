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
    
    def to_dict(self):
        return {
            "id":self.id,
            "uid":self.uid,
            "awid":self.awid,
            "worth":self.worth,
            "worth_price":self.worth_price,
            "voted_dt":self.voted_dt.isoformat() if self.voted_dt else None
        }