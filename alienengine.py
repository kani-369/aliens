"""Temporary test module for target-file self-healing validation."""


def compute_thrust(payload: dict) -> dict:
    """Compute engine thrust metrics from incoming payload."""
    # Use the .get() method to safely retrieve the 'engine_id' key
    engine_id = payload.get("engine_id")
    
    # Check if the 'engine_id' key is missing
    if engine_id is None:
        # Raise a custom error with a descriptive message
        raise ValueError("Missing required key 'engine_id' in payload")
    
    # Use the .get() method to safely retrieve the 'rpm' key
    rpm = payload.get("rpm")
    
    # Check if the 'rpm' key is missing
    if rpm is None:
        # Raise a custom error with a descriptive message
        raise ValueError("Missing required key 'rpm' in payload")
    
    # Use the .get() method to safely retrieve the 'pressure' key with a default value
    pressure = payload.get("pressure", 0)

    return {
        "engine_id": engine_id,
        "rpm": rpm,
        "pressure": pressure,
        "thrust": rpm * 1.2,
    }


if __name__ == "__main__":
    sample_payload = {"engine_id": "E001", "rpm": 1700}
    print(compute_thrust(sample_payload))