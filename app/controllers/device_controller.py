from flask import Blueprint, jsonify, make_response, request
from marshmallow import EXCLUDE

from app.models.device import Device
from app.models.device_schema import DeviceSchema
from app import db


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

    @device_controller.route('/devices/<id>', methods=['DELETE'])
    def delete(id):
        device = Device.query.get(id)
        db.session.delete(device)
        db.session.commit()
        return make_response(jsonify({

        }), 204)

    @device_controller.route('/devices/<id>', methods=['PUT'])
    def update(id):
        device = Device.query.get(id)
        device_schema = DeviceSchema()
        data = request.get_json()

        if (data.get('device_name')):
            device.device_name = data['device_name']
        if (data.get('serie_number')):
            device.serie_number = data['serie_number']
        if (data.get('brand')):
            device.brand = data['brand']
        if (data.get('model')):
            device.model = data['model']

        db.session.add(device)
        db.session.commit()

        update_device = device_schema.dump(device)
        return make_response(jsonify({
            "device": update_device
        }), 200)

