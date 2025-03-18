1. Generate an API Key

curl -X POST "http://127.0.0.1:5000/get-api-key" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "testuser"}'

2. Access the Secured Endpoint (Without API Key)

curl -X GET "http://127.0.0.1:5000/secure-data"

3. Access the Secured Endpoint (With API Key)

curl -X GET "http://127.0.0.1:5000/secure-data" \
     -H "X-API-KEY: 2168af0e-26ce-4380-baf7-19e295fbd2b6"
