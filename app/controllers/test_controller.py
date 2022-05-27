from flask import Blueprint, jsonify, make_response
from app.models.test_schema import TestSchema
from app.models.test import Test
from app import db


class TestController:
    test_controller = Blueprint(name='test_controller', import_name=__name__)

    @test_controller.route('/tests', methods=['GET'])
    def index():
        test_list = Test.query.all()
        test_schema = TestSchema(many=True)
        tests = test_schema.dump(test_list)
        return make_response(jsonify({
            "tests": tests
        }))

    @test_controller.route('/tests/<id>', methods=['GET'])
    def get_test(id):
        test_list = Test.query.get(id)
        test_schema = TestSchema(many=True)
        tests = test_schema.dump(test_list)
        return make_response(jsonify({
            "tests": tests
        }))

    @test_controller.route('/tests', methods=['POST'])
    def create(id):
        data = request.get_json()
        teste_schema = TestSchema(unknown=EXCLUDE)
        teste = teste_schema.load(data)

        response = teste_schema.dump(teste.create())
        return make_response(jsonify({
            "result": response
        }), 201)

    @test_controller.route('/tests/<id>', methods=['PUT'])
    def update(id):
        test = Test.query.get(id)
        data = request.get_json()
        test_schema = TestSchema()

        if(data.get('test_name')):
            test.test_name = data['test_name']
        if(data.get('max_value')):
            test.max_value = data['max_value']
        if(data.get('min_value')):
            test.min_value = data['min_value']
        if(data.get('id_text_type')):
            test.id_test_type = data['id_test_type']
        if(data.get('test_type')):
            test.test_type = data['test_type']

        db.session.add(test)
        db.session.commit()

        updated_test = test_schema.dump(test)
        return make_response(jsonify({
            "products": updated_test
        }), 200)

    @test_controller.route('/tests/<id>', methods=['DELETE'])
    def delete(id):
        test = Test.query.get(id)
        db.session.detele(test)
        db.session.commit()
        return make_response(jsonify({

        }), 204)
