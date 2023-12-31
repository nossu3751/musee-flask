from app.extensions import db
from sqlalchemy import func, ForeignKey
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship
from app.models.demo.user import User

class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="artworks")
    verified = db.Column(db.Boolean, server_default=expression.false(), nullable=False)
    certified = db.Column(db.Boolean, server_default=expression.false(), nullable=False) 
    uploaded_dt = db.Column(db.DateTime, default=func.now())
    verified_dt = db.Column(db.DateTime, nullable=True)
    actual_price = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String, nullable=False) 
    votes = relationship("VerifVote", backref="artwork", cascade="all,delete")
    img_link = db.Column(db.String, nullable=False)
    
    description = db.Column(db.String, nullable=True)
    awSize_width = db.Column(db.Integer, nullable=True)
    awSize_height = db.Column(db.Integer, nullable=True)

    aw_start_date = db.Column(db.DateTime, nullable=True)
    aw_end_date = db.Column(db.DateTime, nullable=True)

    aw_pricing_option = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Artwork {self.id}>'
    
    def to_dict(self):
        return {
            "id":self.id,
            "uid":self.uid,
            "user":self.user.to_dict(),
            "verified":self.verified,
            "verified_dt":self.verified_dt,
            "certified":self.certified,
            "uploaded_dt":self.uploaded_dt.isoformat() if self.uploaded_dt else None,
            "actual_price":self.actual_price,
            "name":self.name,
            "img_link":self.img_link,
            "description":self.description,
            "awSize_width":self.awSize_width,
            "awSize_height":self.awSize_height,
            "aw_start_date":self.aw_start_date,
            "aw_end_date":self.aw_end_date,
            "aw_pricing_option":self.aw_pricing_option
        }