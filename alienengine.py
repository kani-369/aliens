def compute_thrust(payload):
    # Check if the required 'engine_id' key exists in the payload dictionary
    if "engine_id" in payload:
        engine_id = payload["engine_id"]
    else:
        # Raise a custom error with a more informative message
        raise ValueError("Missing required 'engine_id' key in payload")

    # Rest of the function remains the same
    # For demonstration purposes, assume the rest of the function is as follows:
    thrust = 0
    if engine_id == "main_engine":
        thrust = 1000
    elif engine_id == "auxiliary_engine":
        thrust = 500
    return thrust

def main():
    # Example usage:
    payload = {"engine_id": "main_engine"}
    try:
        thrust = compute_thrust(payload)
        print(f"Thrust: {thrust}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()