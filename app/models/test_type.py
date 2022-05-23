from sqlalchemy import Column, BigInteger, String

from app import db


class TestType(db.Model):
    __tablename__ = 'Test_type'
    id_test_type = Column(BigInteger, primary_key=True)
    type_desc = Column(String(128), nullable=True)

    # align with the teacher the business rules
    def __int__(self, id_test_type: int = None, type_desc: str = "") -> None:
        self.id_test_type = id_test_type
        self.type_desc = type_desc

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Type test: {self.type_desc}'
