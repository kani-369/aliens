import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a default API key for demonstration purposes
default_api_key = "default_api_key"

# Define a dictionary to store API keys
api_keys = {
    "user1": "api_key_1",
    "user2": "api_key_2",
}

# Define a function to validate the API key
def validate_api_key(api_key):
    """Validate the API key"""
    return api_key in api_keys.values()

# Define a function to get the API key from the request
def get_api_key(request):
    """Get the API key from the request"""
    # Use the .get() method to avoid KeyError
    api_key = request.headers.get("api_key")
    if api_key is None:
        # If the API key is not in the headers, try to get it from the query parameters
        api_key = request.args.get("api_key")
    return api_key

# Define a route for the /api/data endpoint
@app.route("/api/data", methods=["GET"])
def get_data():
    """Handle GET requests to the /api/data endpoint"""
    try:
        # Get the API key from the request
        api_key = get_api_key(request)
        
        # If the API key is missing, use the default API key
        if api_key is None:
            api_key = default_api_key
            logging.warning("API key is missing, using default API key")
        
        # Validate the API key
        if not validate_api_key(api_key):
            return jsonify({"error": "Invalid API key"}), 401
        
        # If the API key is valid, return the data
        data = {"message": "Hello, World!"}
        return jsonify(data)
    
    except Exception as e:
        # Handle any exceptions and return a 500 error
        logging.error(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)