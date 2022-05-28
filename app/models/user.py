from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, app


class User(db.Model):
    __tablename__ = 'User'
    id_user = Column(BigInteger, primary_key=True)
    login = Column(String(128), nullable=True, unique=True)
    password = Column(String(128), nullable=True)
    id_employee = Column(BigInteger, ForeignKey('Employee.id_employee'), nullable=True)
    employee = relationship("Employee", uselist=False, backref="User", lazy=True)

    # align with the teacher the business rules

    def __init__(self, login, password, employee) -> None:
        self.login = login
        self.password = generate_password_hash(password)
        self.employee = employee

    def __init__(self, login, password) -> None:
        self.login = login
        self.password = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<User: {self.login}'
