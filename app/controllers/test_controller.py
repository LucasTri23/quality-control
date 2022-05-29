from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required
from marshmallow import EXCLUDE
from sqlalchemy import exc

from app.models.test_schema import TestSchema
from app.models.test import Test
from app import db


class TestController:
    test_controller = Blueprint(name='test_controller', import_name=__name__)

    @test_controller.route('/tests', methods=['GET'])
    @jwt_required()
    def index():
        test_list = Test.query.all()
        test_schema = TestSchema(many=True)
        tests = test_schema.dump(test_list)
        return make_response(jsonify({
            "tests": tests
        }))

    @test_controller.route('/tests/<id>', methods=['GET'])
    @jwt_required()
    def get_test(id):
        test = Test.query.filter_by(id_test=id).first_or_404()
        test_schema = TestSchema()
        response = test_schema.dump(test)
        return (jsonify({
            "test": response
        }), 201)

    @test_controller.route('/tests', methods=['POST'])
    @jwt_required()
    def create():
        try:
            data = request.get_json()
            teste_schema = TestSchema(unknown=EXCLUDE)
            teste = teste_schema.load(data)

            response = teste_schema.dump(teste.create())
            return (jsonify({
                "test": response
            }), 201)

        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })
            return response, 409

    @test_controller.route('/tests/<id>', methods=['PUT'])
    @jwt_required()
    def update(id):
        try:
            test = Test.query.get(id)
            data = request.get_json()
            test_schema = TestSchema()

            if data.get('test_name'):
                test.test_name = data['test_name']
            if data.get('max_value'):
                test.max_value = data['max_value']
            if data.get('min_value'):
                test.min_value = data['min_value']
            if data.get('id_text_type'):
                test.id_test_type = data['id_test_type']
            if data.get('test_type'):
                test.test_type = data['test_type']

            db.session.add(test)
            db.session.commit()

            updated_test = test_schema.dump(test)
            return (jsonify({
                "test": updated_test
            }), 200)

        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })
            return response, 409

    @test_controller.route('/tests/<id>', methods=['DELETE'])
    @jwt_required()
    def delete(id):
        try:
            test = Test.query.filter_by(id_test=id).first_or_404()
            db.session.delete(test)
            db.session.commit()
            return (jsonify({

            }), 204)
        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })
            return response, 409
