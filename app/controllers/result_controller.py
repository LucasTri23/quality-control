from flask import Blueprint, jsonify, make_response, request
from marshmallow import EXCLUDE

from app import db
from app.auth.authenticate import token_required
from app.models.result import Result
from app.models.result_schema import ResultSchema


class ResultController:
    result_controller = Blueprint(name='result_controller', import_name=__name__)

    @result_controller.route('/results', methods=['GET'])
    def index():
        result_list = Result.query.all()
        result_schema = ResultSchema(many=True)
        results = result_schema.dump(result_list)
        return make_response(jsonify({
            "results": results
        }))

    @result_controller.route('/results/<id>', methods=['GET'])
    def get_result(id):
        result = Result.query.get(id)
        result_schema = ResultSchema()
        result_serialized = result_schema.dump(result)
        return make_response(jsonify({
            "result": result_serialized
        }))


    @result_controller.route('/results', methods=['POST'])
    @token_required
    def create(current_user):
        data = request.get_json()
        result_schema = ResultSchema(unknown=EXCLUDE)
        result = result_schema.load(data)

        response = result_schema.dump(result.create())
        return make_response(jsonify({
            "result": response
        }), 201)

    @result_controller.route('/results/<id>', methods=['DELETE'])
    def delete(id):
        product = Result.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return make_response(jsonify({}), 204)
