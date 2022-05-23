from marshmallow import fields

from app import ma, db
from app.models.employee import Employee

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        sqla_session = db.session
        load_instance = True

    id_employee = fields.Integer()
    emp_name = fields.Str()
    registry = fields.Str()