from flask import Blueprint, jsonify, make_response, request
from marshmallow import EXCLUDE

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

    @device_controller.route('/devices', methods=['POST'])
    def create():
        data = request.get_json()
        device_schema = DeviceSchema(unknown=EXCLUDE)
        device = device_schema.load(data)
        result = device_schema.dump(device.create())
        return make_response(jsonify({
            "device": result
        }), 201)
