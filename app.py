from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from retell_handler import RetellHandler
from config import SERVER_PORT, SERVER_HOST
from chatbot_state import ChatbotStateMachine
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Retell Handler
retell = RetellHandler()

# Initialize Chatbot State Machine
chatbot = ChatbotStateMachine()

# Project directory setup
PROJECT_DIR = Path(__file__).parent

# Setup Jinja environment
env = Environment(loader=FileSystemLoader(PROJECT_DIR / "templates"))

# Store active conversations
active_conversations = {}

@app.get("/")
def index():
    """Return prompts/index.html if it exists, else a 404 message."""
    html_path = PROJECT_DIR / "index.html"
    if html_path.exists():
        return send_from_directory(PROJECT_DIR, "index.html")
    return (
        "<h1>index.html not found</h1>"
        "<p>Create an index.html in the same folder as app.py.</p>",
        404,
    )

@app.route("/start-conversation", methods=['POST', 'OPTIONS'])
def start_conversation():
    """Start a new conversation with Retell AI"""
    if request.method == 'OPTIONS':
        return '', 204
        
    logger.debug("Received start-conversation request")
    try:
        logger.debug("Creating conversation with Retell AI")
        conversation = retell.create_conversation()
        logger.debug(f"Conversation created: {conversation}")
        
        conversation_id = conversation['conversation_id']
        active_conversations[conversation_id] = {
            'retell_conversation': conversation,
            'messages': []
        }
        
        response = jsonify({
            'conversation_id': conversation_id,
            'status': 'success'
        })
        
        logger.debug(f"Sending response: {response.get_data(as_text=True)}")
        return response
        
    except Exception as e:
        logger.error(f"Error in start_conversation: {str(e)}", exc_info=True)
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.post("/chat")
def chat():
    """Handle chat messages with voice response"""
    data = request.json
    user_input = data.get("message", "")
    conversation_id = data.get("conversation_id")

    if not conversation_id or conversation_id not in active_conversations:
        return jsonify({
            'error': 'Invalid or missing conversation ID',
            'status': 'error'
        }), 400

    try:
        # Get chatbot response
        response_text = chatbot.handle_input(user_input)
        
        # Send response to Retell AI
        message_response = retell.send_message(conversation_id, response_text)
        
        # Get audio URL
        audio_url = retell.get_audio_url(message_response['message_id'])
        
        # Store message in conversation history
        active_conversations[conversation_id]['messages'].append({
            'role': 'user',
            'content': user_input
        })
        active_conversations[conversation_id]['messages'].append({
            'role': 'assistant',
            'content': response_text,
            'audio_url': audio_url
        })

        return jsonify({
            'response': response_text,
            'audio_url': audio_url,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.post("/end-conversation")
def end_conversation():
    """End a conversation with Retell AI"""
    conversation_id = request.json.get("conversation_id")
    
    if not conversation_id or conversation_id not in active_conversations:
        return jsonify({
            'error': 'Invalid or missing conversation ID',
            'status': 'error'
        }), 400

    try:
        retell.end_conversation(conversation_id)
        del active_conversations[conversation_id]
        return jsonify({
            'status': 'success',
            'message': 'Conversation ended successfully'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
