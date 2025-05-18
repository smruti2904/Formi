import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retell AI Configuration
RETELL_API_KEY = "key_85b29d6a9dcbcc299bf4522e94bb"

# Retell AI Voice Configuration
VOICE_CONFIG = {
    "provider": "eleven-labs",
    "model": "eleven-labs-v1",
    "voice_id": "rachel",
    "language": "en-US",
    "speed": 1.0,
    "stability": 0.5,
    "similarity_boost": 0.75
}

# Server Configuration
SERVER_HOST = "0.0.0.0"  # Changed to allow external connections
SERVER_PORT = 5000

# Chatbot Configuration
MAX_HISTORY_LENGTH = 10
TEMPERATURE = 0.7 