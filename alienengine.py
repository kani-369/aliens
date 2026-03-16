from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory data store
data_store = {
    'api_key_1': {'data': 'Sample data for api_key_1'},
    'api_key_2': {'data': 'Sample data for api_key_2'}
}

# Define a function to validate the API key
def validate_api_key(api_key):
    """Validate the API key"""
    return api_key in data_store

# Define a function to get data for a given API key
def get_data(api_key):
    """Get data for a given API key"""
    return data_store.get(api_key)

# Define the API endpoint for /api/data
@app.route('/api/data', methods=['GET'])
def get_api_data():
    """API endpoint to retrieve data"""
    # Get the API key from the request context
    api_key = request.args.get('api_key')

    # Check if the API key is provided
    if not api_key:
        # Return an error response if the API key is not provided
        return jsonify({'error': 'API key is required'}), 400

    # Validate the API key
    if not validate_api_key(api_key):
        # Return an error response if the API key is invalid
        return jsonify({'error': 'Invalid API key'}), 401

    # Get the data for the given API key
    data = get_data(api_key)

    # Return the data as a JSON response
    return jsonify({'data': data.get('data')}), 200

if __name__ == '__main__':
    app.run(debug=True)