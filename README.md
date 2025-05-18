# Chatbot with Retell AI Integration

This project implements a chatbot system integrated with Retell AI for voice interactions, along with a knowledge base management system.

## Project Structure

```
├── app.py              # Main Flask application
├── server.py           # Server implementation
├── chatbot_state.py    # Chatbot state management
├── kb_api.py           # Knowledge base API handlers
├── main.py             # Main entry point
├── template_utils.py   # Utility functions for templates
├── test_chatbot.py     # Test cases
├── templates/          # HTML templates
├── prompts/           # Prompt templates
└── knowledge_base/    # Knowledge base data
    ├── delhi_kb.json
    └── bangalore_kb.json
```

## Prerequisites

- Python 3.8 or higher
- Retell AI API key (Sign up at https://retellai.com)
- Flask web framework
- Required Python packages (see requirements below)

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Install required packages:
```bash
pip install flask requests python-dotenv
```

3. Configure Retell AI:
   - Sign up for a Retell AI account
   - Get your API key from the dashboard
   - Create a `.env` file in the project root and add:
   ```
   RETELL_API_KEY=your_api_key_here
   ```

4. Initialize the knowledge base:
   - Place your knowledge base JSON files in the `knowledge_base` directory
   - Format should match the existing delhi_kb.json and bangalore_kb.json structure

5. Start the application:
```bash
python app.py
```

## Features

- Voice-enabled chatbot using Retell AI
- Knowledge base integration
- Real-time conversation state management
- Web interface for interactions
- Customizable prompt templates
- Multiple knowledge base support

## API Endpoints

- `/chat`: Main chatbot interaction endpoint
- `/update_kb`: Update knowledge base
- `/get_kb`: Retrieve knowledge base contents

## Testing

Run the test suite using:
```bash
python -m pytest test_chatbot.py
```

## Security Notes

- Keep your Retell AI API key secure
- Don't commit the `.env` file to version control
- Implement proper authentication for production use

## License

[Your License Here]

## Support

For any questions or issues, please open an issue in the repository or contact the maintainers. 