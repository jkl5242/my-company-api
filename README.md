# my-company-api

How to run:
1. docker build -t my-company-api .
2. docker run -p 8080:8080 my-company-api

Request Examples:
1. curl -X GET "http://localhost:8080/company/list?q=solution"
2. curl -X PUT "http://localhost:8080/company/webitects" -H "Content-Type: application/json" -d '{
    "description": "testing123"
}'
