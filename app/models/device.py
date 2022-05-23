from sqlalchemy import Column, BigInteger, String, Numeric, CheckConstraint, Integer, DateTime
from sqlalchemy.sql.functions import current_timestamp

from app import db


class Device(db.Model):
    __tablename__ = 'Device'
    id_device = Column(BigInteger, primary_key=True)
    device_name = Column(String(128), nullable=True)
    serie_number = Column(String(128), nullable=True)
    brand = Column(String(128), nullable=True)
    model = Column(String(128), nullable=True)

#align with the teacher the business rules
    def __init__(self, device_name: str = "", serie_number: str = "", brand: str = "", model: str = "") -> None:
        self.device_name = device_name
        self.serie_number = serie_number
        self.brand = brand
        self.model = model

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Device: {self.name}'
