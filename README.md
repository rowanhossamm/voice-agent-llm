# Voice Automation Agent

This project is a **Voice Automation Agent** that can:

- Answer questions about a schedule.
- Help book a schedule in English through voice.
- Integrates with Google Calendar (optional).

## Demo

You can watch a short demo of the voice agent interactions here:  
[Demo Video](https://github.com/rowanhossamm/voice-agent-llm/blob/main/demo.mp4)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/rowanhossamm/voice-agent-llm.git
cd voice-agent-llm
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
API Keys
For the agent to work with Google Calendar and Gemini LLM, you need to create your own API key.

A file named config.py is included as an example.

You can get your own API key here: Google AI Studio API Keys

Example config.py:

python
Copy code
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
Make sure not to commit your keys to GitHub.

Usage
Run the agent:

bash
Copy code
python app.py
Speak commands like:

"List my appointments" → lists your upcoming events.

"Book an appointment" → the agent will ask for date and time.

Notes
The agent uses speech_recognition for speech-to-text and gTTS for text-to-speech.

For calendar integration, make sure you have credentials.json and token.json configured locally (do not push these to GitHub).

