from flask import Blueprint, jsonify, make_response, request


from app import db
from app.models.device import Device
from app.models.device_schema import DeviceSchema

class DeviceController:
    device_controller = Blueprint(name='device_controller', import_name=__name__)

    @device_controller.route('/devices', methods=['GET'])
    def index():
        device_list = Device.query.all()
        device_schema = DeviceSchema(many=True)
        devices = device_schema.dump(device_list)

        return make_response(jsonify({
            "devices": devices
        }))