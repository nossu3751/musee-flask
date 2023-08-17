from app.extensions import db
from sqlalchemy.orm import relationship

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False) 
    artworks = relationship("Artwork", back_populates="user")
    votes = relationship("VerifVote", backref="voter")
    
    def __repr__(self):
        return f'<User {self.id}>'

    