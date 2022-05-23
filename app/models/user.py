from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

from app import db, app


class User(db.Model):
    __tablename__ = 'User'
    id_user = Column(BigInteger, primary_key=True)
    login = Column(String(128), nullable=True)
    password = Column(String(128), nullable=True)
    id_employee = Column(BigInteger, ForeignKey('Employee.id_employee'), nullable=True)
    employee = relationship("Employee", uselist=False, backref="User", lazy=True)

    # align with the teacher the business rules

    def __init__(self, login: str = "", password: str = "") -> None:
        self.login = login
        self.password = password

    def __init__(self, login: str = "", password: str = "",
                 id_employee: int = None) -> None:
        self.login = login
        self.password = password
        self.id_employee = id_employee

    def __init__(self, login, password, employee) -> None:
        self.login = login
        self.password = password
        self.employee = employee

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<User: {self.login}'
