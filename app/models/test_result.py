from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from app import db


class TestResult(db.Model):
    __tablename__ = 'Test_result',
    id_test = Column(BigInteger, ForeignKey('Test.id_test'), nullable=False, primary_key=True)
    id_result = Column(BigInteger, ForeignKey('Result.id_result'), nullable=False, primary_key=True)

    # align with the teacher the business rules
    def __init__(self, id_teste, id_result) -> None:
        self.id_test = id_teste
        self.id_result = id_result

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Test: {self.id_result}'
