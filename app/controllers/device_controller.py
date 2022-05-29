from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required
from marshmallow import EXCLUDE
from sqlalchemy import exc
from app.models.device import Device
from app.models.device_schema import DeviceSchema
from app import db


class DeviceController:
    device_controller = Blueprint(name='device_controller', import_name=__name__)

    @device_controller.route('/devices', methods=['GET'])
    @jwt_required()
    def index():
        device_list = Device.query.all()
        device_schema = DeviceSchema(many=True)
        devices = device_schema.dump(device_list)

        return (jsonify({
            "devices": devices
        }), 200)

    @device_controller.route('/devices/<id>', methods=['GET'])
    @jwt_required()
    def get_result(id):
        device = Device.query.filter_by(id_device=id).first_or_404()
        device_schema = DeviceSchema()
        response = device_schema.dump(device)

        return (jsonify({
            "device": response
        }), 200)

    @device_controller.route('/devices', methods=['POST'])
    @jwt_required()
    def create():
        try:
            data = request.get_json()
            device_schema = DeviceSchema(unknown=EXCLUDE)
            device = device_schema.load(data)
            result = device_schema.dump(device.create())
            return make_response(jsonify({
                "device": result
            }), 201)
        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })

            return response, 409

    @device_controller.route('/devices/<id>', methods=['DELETE'])
    @jwt_required()
    def delete(id):
        try:
            device = Device.query.filter_by(id_device=id).first_or_404()
            db.session.delete(device)
            db.session.commit()
            return (jsonify({

            }), 204)
        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })
            return response, 409

    @device_controller.route('/devices/<id>', methods=['PUT'])
    @jwt_required()
    def update(id):
        try:
            device = Device.query.filter_by(id_device=id).first_or_404()
            device_schema = DeviceSchema()
            data = request.get_json()

            if data.get('device_name'):
                device.device_name = data['device_name']
            if data.get('serie_number'):
                device.serie_number = data['serie_number']
            if data.get('brand'):
                device.brand = data['brand']
            if data.get('model'):
                device.model = data['model']

            db.session.add(device)
            db.session.commit()

            update_device = device_schema.dump(device)
            return (jsonify({
                "device": update_device
            }), 200)

        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })
            return response, 409
