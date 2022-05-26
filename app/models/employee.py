from sqlalchemy import Column, BigInteger, String, Numeric, CheckConstraint, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from app import db

class Employee(db.Model):
    __tablename__ = 'Employee'
    id_employee = Column(BigInteger, primary_key=True)
    emp_name = Column(String(128), nullable=True)
    registry = Column(String(128), nullable=True)


#align with the teacher the business rules
    def __init__(self, emp_name, registry) -> None:
        self.emp_name = emp_name
        self.registry = registry

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Employee: {self.emp_name}'
