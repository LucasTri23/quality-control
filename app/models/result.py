from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from app import db, app


class Result(db.Model):
    __tablename__ = 'Result'
    id_result = Column(BigInteger, primary_key=True)
    date_hour = Column(DateTime, server_default=current_timestamp())
    measured_value = Column(Numeric(10, 2), nullable=False)
    result = Column(String(128), nullable=False)
    id_test = Column(BigInteger, ForeignKey('Test.id_test'), nullable=False)
    test = relationship("Test", uselist=False, backref="Result", lazy=True)
    id_employee = Column(BigInteger, ForeignKey('Employee.id_employee'), nullable=False)
    employee = relationship("Employee", uselist=False, backref="Result", lazy=True)
    id_device = Column(BigInteger, ForeignKey('Device.id_device'), nullable=False)
    device = relationship("Device", uselist=False, backref="Result", lazy=True)

    # align with the teacher the business rules
    def __init__(self, measured_value, result, id_employee, id_test, id_device) -> None:
        self.measured_value = measured_value
        self.result = result
        self.id_employee = id_employee
        self.id_test = id_test
        self.id_device = id_device

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Result: {self.result}'
