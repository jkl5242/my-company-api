from flask import Flask
from api import company_api

app = Flask(__name__)

# Register the company API blueprint
app.register_blueprint(company_api)

if __name__ == '__main__':
    app.run(debug=True)
