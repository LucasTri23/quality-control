from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required
from marshmallow import EXCLUDE
from sqlalchemy import exc
from app import db
from app.models.result import Result
from app.models.result_schema import ResultSchema

class ResultController:
    result_controller = Blueprint(name='result_controller', import_name=__name__)

    @result_controller.route('/results', methods=['GET'])
    @jwt_required()
    def index():
        id_device = request.args.get('id_device', None)
        id_employee = request.args.get('id_emp', None)
        date_hour = request.args.get('date', None)
        result_list = Result.get_results(id_device, id_employee, date_hour)
        result_schema = ResultSchema(many=True)
        results = result_schema.dump(result_list)
        return (jsonify({
            "results": results
        }), 200)

    @result_controller.route('/results/<id>', methods=['GET'])
    @jwt_required()
    def get_result(id):
        result = Result.query.filter_by(id_result=id).first_or_404()
        result_schema = ResultSchema()
        response = result_schema.dump(result)
        return (jsonify({
            "result": response
        }), 200)

    @result_controller.route('/results', methods=['POST'])
    @jwt_required()
    def create():
        try:
            data = request.get_json()
            result_schema = ResultSchema(unknown=EXCLUDE)
            result = result_schema.load(data)
            response = result_schema.dump(result.create())
            return (jsonify({
                "result": response
            }), 201)
        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })
            return response, 409

    @result_controller.route('/results/<id>', methods=['DELETE'])
    @jwt_required()
    def delete(id):
        try:
            result = Result.query.filter_by(id_result=id).first_or_404()
            db.session.delete(result)
            db.session.commit()
            return (jsonify({
            }), 204)
        except exc.IntegrityError:
            db.session.rollback()
            response = jsonify({
                'message': 'Database Error'
            })
            return response, 409
