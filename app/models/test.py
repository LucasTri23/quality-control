from sqlalchemy import Column, BigInteger, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from app import db, app


class Test(db.Model):
    __tablename__ = 'Test'
    id_test = Column(BigInteger, primary_key=True)
    test_name = Column(String(100), nullable=True)
    max_value = Column(Numeric(10, 2), nullable=True)
    min_value = Column(Numeric(10, 2), nullable=True)
    id_test_type = Column(BigInteger, ForeignKey('Test_type.id_test_type'), nullable=False)
    test_type = relationship("TestType", uselist=False, backref="Test", lazy=True)

    # align with the teacher the business rules
    def __init__(self, test_name, max_value, min_value, id_test_type, test_type) -> None:
        self.test_name = test_name
        self.max_value = max_value
        self.min_value = min_value
        self.id_test_type = id_test_type
        self.test_type = test_type

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Test: {self.test_name}'
