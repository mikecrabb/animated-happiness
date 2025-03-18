from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Simulated database of API keys (In production, store this securely in a database)
API_KEYS = {}

# Middleware to check API keys
@app.before_request
def check_api_key():
    if request.endpoint == "get_api_key":  # Allow access to API key generation
        return
    
    api_key = request.headers.get("X-API-KEY")
    
    if not api_key or api_key not in API_KEYS.values():
        return jsonify({"message": "Invalid or missing API Key"}), 401

# Route to generate and return an API key
@app.route("/get-api-key", methods=["POST"])
def get_api_key():
    """Generate a new API key for a user"""
    user_id = request.json.get("user_id")  # Simulated user input
    if not user_id:
        return jsonify({"message": "Missing user_id"}), 400
    
    if user_id in API_KEYS:
        return jsonify({"message": "API Key already generated", "api_key": API_KEYS[user_id]}), 200
    
    new_api_key = str(uuid.uuid4())  # Generate a unique API key
    API_KEYS[user_id] = new_api_key
    return jsonify({"message": "API Key generated", "api_key": new_api_key}), 201

# A secured endpoint that requires an API key
@app.route("/secure-data", methods=["GET"])
def secure_data():
    """Return secured data only if API key is valid"""
    return jsonify({"message": "Welcome! You have access to secure data"}), 200

if __name__ == "__main__":
    app.run(debug=True)