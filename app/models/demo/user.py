from app.extensions import db
from sqlalchemy.orm import relationship

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    first_name = db.Column(db.String, nullable=False) 
    last_name = db.Column(db.String, nullable=False) 
    tokens = db.Column(db.Integer, nullable=False, default=0)
    artworks = relationship("Artwork", back_populates="user")
    votes = relationship("VerifVote", backref="voter")

    
    def __repr__(self):
        return f'<User {self.id}>'
    
    def to_dict(self):
        return {
            "id":self.id,
            "email":self.email,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "tokens":self.tokens
        }


    