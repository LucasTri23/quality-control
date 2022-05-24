from flask import Blueprint, jsonify, make_response
from app.models.test_schema import TestSchema
from app.models.test import Test


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
