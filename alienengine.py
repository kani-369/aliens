def compute_thrust(payload):
    """
    Compute the thrust of an alien engine based on the provided payload.
    
    Args:
        payload (dict): A dictionary containing the engine_id and other relevant data.
        
    Returns:
        float: The computed thrust of the alien engine.
    """
    # Check if the payload contains the required 'engine_id' key
    if 'engine_id' not in payload:
        raise ValueError("Missing required 'engine_id' key in payload")
    
    # Extract the engine_id from the payload using the get method for defensive programming
    engine_id = payload.get('engine_id')
    
    # Simulate the computation of thrust (this is a placeholder, replace with actual logic)
    thrust = 1000.0  # Replace with actual computation
    
    return thrust


def get_api_data(request):
    """
    Retrieve data from the API based on the provided request.
    
    Args:
        request (dict): A dictionary containing the api_key and other relevant data.
        
    Returns:
        dict: The retrieved data from the API.
    """
    # Check if the request contains the required 'api_key' key
    if 'api_key' not in request:
        raise ValueError("Missing required 'api_key' key in request")
    
    # Extract the api_key from the request using the get method for defensive programming
    api_key = request.get('api_key')
    
    # Simulate the retrieval of data from the API (this is a placeholder, replace with actual logic)
    data = {"message": "Data retrieved successfully"}  # Replace with actual data retrieval
    
    return data


def main():
    # Example usage of the compute_thrust function
    payload = {"engine_id": "AE-1234"}
    try:
        thrust = compute_thrust(payload)
        print(f"Computed thrust: {thrust}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example usage of the get_api_data function
    request = {"api_key": "API-KEY-1234"}
    try:
        data = get_api_data(request)
        print(f"Retrieved data: {data}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()