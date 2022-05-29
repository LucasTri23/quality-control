from app import db

class RevokedToken(db.Model):

    __tablename__ = "Revoked_tokens"

    id_token = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(100), nullable=False)
