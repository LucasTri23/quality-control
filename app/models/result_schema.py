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
    id_test = fields.Integer()
    id_employee = fields.Integer()
    id_device = fields.Integer()
    date_hour = fields.DateTime()
    employee = fields.Nested(EmployeeSchema)
    device = fields.Nested(DeviceSchema)
    tests = fields.Nested(TestSchema, many=True)
