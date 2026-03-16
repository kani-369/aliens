"""Temporary test module for target-file self-healing validation."""

def compute_thrust(payload: dict) -> dict:
    """Compute engine thrust metrics from incoming payload."""
    # Check if engine_id exists in the payload to avoid KeyError
    if "engine_id" not in payload:
        # Handle the case where engine_id is missing
        # For example, return an error message or raise a custom exception
        raise ValueError("engine_id is required")
    
    engine_id = payload["engine_id"]
    # Use get() method to provide a default value for rpm if it's missing
    rpm = payload.get("rpm")
    if rpm is None:
        # Handle the case where rpm is missing
        # For example, return an error message or raise a custom exception
        raise ValueError("rpm is required")
    
    # Use get() method to provide a default value for pressure if it's missing
    pressure = payload.get("pressure", 0)

    return {
        "engine_id": engine_id,
        "rpm": rpm,
        "pressure": pressure,
        "thrust": rpm * 1.2,
    }


if __name__ == "__main__":
    sample_payload = {"engine_id": 1, "rpm": 1700}
    print(compute_thrust(sample_payload))