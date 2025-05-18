import logging
from retell import Retell
from config import RETELL_API_KEY, VOICE_CONFIG

logger = logging.getLogger(__name__)

class RetellHandler:
    def __init__(self):
        self.api_key = RETELL_API_KEY
        self.client = Retell(api_key=self.api_key)
        logger.debug(f"Initialized RetellHandler with API key: {self.api_key[:8]}...")

    def create_conversation(self):
        """Create a new conversation session with Retell AI"""
        try:
            # Create a conversation using the SDK
            payload = {
                "model": "gpt-3.5-turbo",
                "voice": {
                    "provider": VOICE_CONFIG["provider"],
                    "voice_id": VOICE_CONFIG["voice_id"],
                    "language": VOICE_CONFIG["language"],
                    "speed": VOICE_CONFIG["speed"],
                    "stability": VOICE_CONFIG["stability"],
                    "similarity_boost": VOICE_CONFIG["similarity_boost"]
                }
            }
            logger.debug(f"Creating conversation with payload: {payload}")
            
            conversation = self.client.conversations.create(**payload)
            logger.debug(f"Successfully created conversation: {conversation}")
            return {
                "conversation_id": conversation.id,
                "status": "success"
            }
        except Exception as e:
            logger.error(f"Error creating conversation: {str(e)}")
            raise

    def send_message(self, conversation_id, message):
        """Send a message to an existing conversation"""
        try:
            payload = {
                "conversation_id": conversation_id,
                "role": "assistant",
                "content": message
            }
            logger.debug(f"Sending message to conversation {conversation_id}: {message[:50]}...")
            
            message = self.client.messages.create(**payload)
            logger.debug(f"Successfully sent message: {message}")
            return {
                "message_id": message.id,
                "status": "success"
            }
        except Exception as e:
            logger.error(f"Error sending message: {str(e)}")
            raise

    def get_audio_url(self, message_id):
        """Get the audio URL for a message"""
        try:
            logger.debug(f"Getting audio URL for message {message_id}")
            
            audio = self.client.messages.get_audio(message_id)
            logger.debug(f"Successfully got audio URL: {audio}")
            return audio.url
        except Exception as e:
            logger.error(f"Error getting audio URL: {str(e)}")
            raise

    def end_conversation(self, conversation_id):
        """End an existing conversation"""
        try:
            logger.debug(f"Ending conversation {conversation_id}")
            
            result = self.client.conversations.end(conversation_id)
            logger.debug(f"Successfully ended conversation: {result}")
            return {
                "status": "success",
                "message": "Conversation ended successfully"
            }
        except Exception as e:
            logger.error(f"Error ending conversation: {str(e)}")
            raise 