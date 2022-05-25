from flask import Blueprint, jsonify, make_response, request
from app.models.test_schema import TestSchema
from app.models.test import Test


class TestController:
    test_controller = Blueprint(name='test_controller', import_name=__name__)

    @test_controller.route('/tests', methods=['GET'])
    def index(self):
        test_list = Test.query.all()
        test_schema = TestSchema(many=True)
        tests = test_schema.dump(test_list)
        return make_response(jsonify({
            "tests": tests
        }))

    @test_controller.route('/tests', methods=['POST'])
    def create(self):
        data = request.get_json()
        test_schema = TestSchema()
        data_dumped = test_schema.dump(data)
        test = test_schema.load(data_dumped)

        response = test_schema.dump(test.create())
        return make_response(jsonify({
            "test": response
        }), 201)

    @test_controller.route('/tests/<int:id>', methods=['DELETE'])
    def delete(self, id):
        test = Test.query.get(id)
        test.delete()

        return make_response(jsonify({
            "message": "Test deleted"
        }))

    @test_controller.route('/tests/<int:id>', methods=['PUT'])
    def update(self, id):
        test = Test.query.get(id)
        data = request.get_json()
        test_schema = TestSchema()
        data_dumped = test_schema.dump(data)
        test = test_schema.load(data_dumped)
        test.update(test)

        return make_response(jsonify({
            "message": "Test updated"
        }))
