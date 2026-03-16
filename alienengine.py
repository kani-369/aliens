import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_payload(payload):
    """
    Process the payload dictionary.
    
    Args:
        payload (dict): The payload dictionary containing the engine_id and other data.
    
    Returns:
        dict: The processed payload dictionary.
    """
    # Check if payload is a dictionary
    if not isinstance(payload, dict):
        logger.error("Payload is not a dictionary")
        return None
    
    # Check if 'engine_id' key is present in the payload dictionary
    if 'engine_id' not in payload:
        logger.error("Missing 'engine_id' key in payload")
        return None
    
    # Get the 'engine_id' value from the payload dictionary using .get() for defensive programming
    engine_id = payload.get('engine_id')
    
    # Process the payload dictionary
    # Add your processing logic here
    processed_payload = {'engine_id': engine_id}
    
    return processed_payload

def get_api_data(api_key):
    """
    Get API data using the provided API key.
    
    Args:
        api_key (str): The API key used to authenticate the request.
    
    Returns:
        dict: The API data dictionary.
    """
    # Check if api_key is not empty
    if not api_key:
        logger.error("Missing 'api_key' parameter")
        return None
    
    # Get API data using the provided API key
    # Add your API data retrieval logic here
    api_data = {'api_key': api_key, 'data': 'Sample API data'}
    
    return api_data

def main():
    # Sample payload dictionary
    payload = {'engine_id': '12345'}
    
    # Process the payload dictionary
    processed_payload = process_payload(payload)
    
    # Log the processed payload dictionary
    logger.info(processed_payload)
    
    # Sample API key
    api_key = 'sample_api_key'
    
    # Get API data using the provided API key
    api_data = get_api_data(api_key)
    
    # Log the API data dictionary
    logger.info(api_data)

if __name__ == "__main__":
    main()