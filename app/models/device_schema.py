from marshmallow import fields

from app import ma, db
from app.models.device import Device

class DeviceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Device
        sqla_session = db.session
        load_instance = True

    id_device = fields.Integer()
    device_name = fields.Str()
    serie_number = fields.Str()
    brand = fields.Str()
    model = fields.Str()
