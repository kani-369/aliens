import json

def compute_thrust(payload):
    # Check if payload is a dictionary
    if not isinstance(payload, dict):
        raise ValueError("Payload must be a dictionary")

    # Use .get() to safely access the 'engine_id' key
    engine_id = payload.get('engine_id')
    
    # Check if 'engine_id' key is present
    if engine_id is None:
        raise KeyError("Missing required key 'engine_id' in payload")

    # Rest of the function remains the same
    # Replace this comment with the actual implementation
    thrust = calculate_thrust(engine_id)  # Assuming calculate_thrust is a function
    return thrust

def calculate_thrust(engine_id):
    # Replace this comment with the actual implementation
    # For demonstration purposes, a simple calculation is used
    return engine_id * 10

def main():
    # Example usage
    payload = {'engine_id': 5}
    try:
        thrust = compute_thrust(payload)
        print(f"Thrust: {thrust}")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()