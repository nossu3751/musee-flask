from app.extensions import db
from sqlalchemy import func, ForeignKey
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship

class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="artworks")
    verified = db.Column(db.Boolean, server_default=expression.false(), nullable=False) 
    uploaded_dt = db.Column(db.DateTime, default=func.now())
    actual_price = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String, nullable=False) 
    votes = relationship("VerifVote", backref="artwork")
   
    def __repr__(self):
        return f'<Artwork {self.id}>'