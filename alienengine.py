def compute_thrust(payload):
    """
    Compute the thrust of an alien engine based on the provided payload.
    
    Args:
        payload (dict): A dictionary containing the engine's configuration.
        
    Returns:
        float: The computed thrust of the engine.
    """
    # Check if the payload contains the required 'engine_id' key
    if 'engine_id' not in payload:
        raise ValueError("Missing required 'engine_id' key in payload")
    
    # Extract the engine_id from the payload using the get method for defensive programming
    engine_id = payload.get('engine_id')
    
    # Simulate the computation of thrust (this is a placeholder, replace with actual logic)
    thrust = 1000.0  # Replace with actual computation
    
    return thrust


def get_engine_data(engine_id, api_key):
    """
    Retrieve data for a specific alien engine based on its ID and API key.
    
    Args:
        engine_id (str): The ID of the alien engine.
        api_key (str): The API key for authentication.
        
    Returns:
        dict: A dictionary containing the engine's data.
    """
    # Check if the api_key is provided
    if not api_key:
        raise ValueError("Missing required 'api_key' key")
    
    # Simulate the retrieval of engine data (this is a placeholder, replace with actual logic)
    engine_data = {
        'engine_id': engine_id,
        'thrust': 1000.0,
        'fuel_efficiency': 0.8
    }  # Replace with actual data retrieval
    
    return engine_data


def main():
    # Example usage of the compute_thrust function
    payload = {
        'engine_id': 'AE-123',
        'fuel_type': 'plasma',
        'thrust_vector': [1.0, 0.0, 0.0]
    }
    try:
        thrust = compute_thrust(payload)
        print(f"Computed thrust: {thrust}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example usage of the get_engine_data function
    engine_id = 'AE-123'
    api_key = 'your_api_key_here'
    try:
        engine_data = get_engine_data(engine_id, api_key)
        print(f"Engine data: {engine_data}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()