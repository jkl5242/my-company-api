from flask import Blueprint
from flask_restful import Api
from .company import CompanyList, CompanyUpdate

company_api = Blueprint('company_api', __name__)
api = Api(company_api)

api.add_resource(CompanyList, '/company/list')
api.add_resource(CompanyUpdate, '/company/<string:company_name_id>')
