from marshmallow import fields

from app import ma, db
from app.models.device_schema import DeviceSchema
from app.models.employee_schema import EmployeeSchema
from app.models.test_schema import TestSchema
from app.models.result import Result


class ResultSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Result
        sqla_session = db.session
        load_instance = True

    id_result = fields.Integer()
    measured_value = fields.Decimal()
    result_desc = fields.Str()
    id_employee = fields.Integer(required=True)
    id_device = fields.Integer(required=True)
    date_hour = fields.DateTime()
    employee = fields.Nested(EmployeeSchema, dump_only=True)
    device = fields.Nested(DeviceSchema, dump_only=True)
    tests = fields.Nested(TestSchema, many=True)
