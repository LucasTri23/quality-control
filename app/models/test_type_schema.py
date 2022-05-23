from marshmallow import fields
from app import ma, db
from app.models.test_type import TestType

class TestTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TestType
        sqla_session = db.session
        load_instance = True

    id_test_type = fields.Integer()
    type_desc = fields.Str()
