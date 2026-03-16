def compute_thrust(payload):
    # Add input validation to ensure the 'engine_id' key is present in the payload
    if 'engine_id' not in payload:
        raise ValueError("Missing 'engine_id' key in payload")

    # Use the .get() method to safely access the 'engine_id' key
    engine_id = payload.get('engine_id')
    
    # Rest of the function remains the same
    thrust = 0
    if engine_id == 'main':
        thrust = 1000
    elif engine_id == 'auxiliary':
        thrust = 500
    return thrust

def main():
    # Example usage
    payload = {'engine_id': 'main'}
    try:
        thrust = compute_thrust(payload)
        print(f"Thrust: {thrust}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()