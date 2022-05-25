from flask import Blueprint, jsonify, make_response, request

from app.models.result import Result
from app.models.result_schema import ResultSchema


class ResultController:
    result_controller = Blueprint(name='result_controller', import_name=__name__)

    @result_controller.route('/results', methods=['GET'])
    def index(self):
        result_list = Result.query.all()
        result_schema = ResultSchema(many=True)
        results = result_schema.dump(result_list)
        return make_response(jsonify({
            "results": results
        }))

    @result_controller.route('/results', methods=['POST'])
    def create(self):
        data = request.get_json()
        result_schema = ResultSchema()
        data_dumped = result_schema.dump(data)
        result = result_schema.load(data_dumped)

        response = result_schema.dump(result.create())
        return make_response(jsonify({
            "result": response
        }), 201)

    @result_controller.route('/results/<int:id>', methods=['DELETE'])
    def delete(self, id):
        result = Result.query.get(id)
        result.delete()

        return make_response(jsonify({
            "message": "Result deleted"
        }))

    @result_controller.route('/results/<int:id>', methods=['PUT'])
    def update(self, id):
        result = Result.query.get(id)
        data = request.get_json()
        result_schema = ResultSchema()
        data_dumped = result_schema.dump(data)
        result = result_schema.load(data_dumped)
        result.update(result)

        return make_response(jsonify({
            "message": "Result updated"
        }))
