def get_property_info(location):
    """
    Simple function to return property information based on location.
    In a real implementation, this would query a database or API.
    """
    # Simple mock data
    properties = {
        "bangalore": {
            "name": "BBQ Nation Bangalore",
            "address": "123 MG Road, Bangalore",
            "phone": "080-12345678"
        },
        "delhi": {
            "name": "BBQ Nation Delhi",
            "address": "456 Connaught Place, Delhi",
            "phone": "011-87654321"
        }
    }
    
    location = location.lower().strip()
    return properties.get(location, None) 