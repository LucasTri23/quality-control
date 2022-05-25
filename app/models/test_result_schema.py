from marshmallow import fields

from app import ma, db
from app.models.result_schema import ResultSchema
from app.models.test_result import TestResult
from app.models.test_schema import TestSchema


class TestResultSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TestResult
        sqla_session = db.session
        load_instance = True

    id_test = fields.Integer()
    id_result = fields.Str()
    # test = fields.Nested(TestSchema)
    # result = fields.Nested(ResultSchema)
