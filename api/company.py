from flask import request
from flask_restful import Resource
import json

# Load company data from companies.json
with open('data/companies.json', 'r') as file:
    companies_data = json.load(file)

class CompanyList(Resource):
    def get(self):
        query = request.args.get('q')
        if query:
            matching_companies = [company for company in companies_data if query in company['company_name'].lower() or query in company['description'].lower()]
            return matching_companies[:50]
        else:
            return {'error': 'No query provided'}, 400

class CompanyUpdate(Resource):
    def put(self, company_name_id):
        try:
            data = request.get_json()
            company = next((c for c in companies_data if c['company_name_id'] == company_name_id), None)
            if company:
                for key, value in data.items():
                    if key in company:
                        company[key] = value
                with open('data/companies.json', 'w') as file:
                    json.dump(companies_data, file, indent=4)
                return {'message': 'Company updated successfully'}
            else:
                return {'error': 'Company not found'}, 404
        except Exception as e:
            return {'error': 'Invalid request data'}, 400
