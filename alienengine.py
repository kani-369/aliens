class AlienEngine:
    def __init__(self):
        pass

    def compute_thrust(self, payload):
        # Check if 'engine_id' key exists in the payload dictionary
        if 'engine_id' not in payload:
            # Handle the case where 'engine_id' key is missing
            print("Error: 'engine_id' key is missing from the payload dictionary.")
            return None
        
        # Safely retrieve the 'engine_id' value using the get() method
        engine_id = payload.get('engine_id')
        
        # Example computation (replace with actual logic)
        thrust = engine_id * 1000  # Replace with actual thrust computation
        
        return thrust

    def start_engine(self, payload):
        # Check if 'engine_id' key exists in the payload dictionary
        if 'engine_id' not in payload:
            # Handle the case where 'engine_id' key is missing
            print("Error: 'engine_id' key is missing from the payload dictionary.")
            return None
        
        # Safely retrieve the 'engine_id' value using the get() method
        engine_id = payload.get('engine_id')
        
        # Example engine start logic (replace with actual logic)
        print(f"Starting engine {engine_id}...")
        
        return True

def main():
    engine = AlienEngine()
    payload = {'fuel_level': 100, 'engine_id': 123}
    thrust = engine.compute_thrust(payload)
    print(f"Computed thrust: {thrust}")
    engine.start_engine(payload)

if __name__ == "__main__":
    main()