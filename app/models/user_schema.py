from marshmallow import fields

from app import ma, db
from app.models.employee_schema import EmployeeSchema
from app.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True

    id_user = fields.Integer()
    login = fields.Str()
    password = fields.Str(load_only=True)
    user_role = fields.Integer()
    id_employee = fields.Str()
    employee = fields.Nested(EmployeeSchema)
