from marshmallow import fields

from app import ma, db
from app.models.test_type_schema import TestTypeSchema
from app.models.test import Test


class TestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Test
        sqla_session = db.session
        load_instance = True

    id_test = fields.Integer()
    test_name = fields.Str()
    max_value = fields.Decimal(allow_none=True)
    min_value = fields.Decimal(allow_none=True)
    id_test_type = fields.Integer()
    test_type = fields.Nested(TestTypeSchema)
