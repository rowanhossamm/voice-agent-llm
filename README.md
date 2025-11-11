# Voice Automation Agent

This project is a **Voice Automation Agent** that can:

- Answer questions about a schedule.
- Help book a schedule in English through voice.
- Integrates with Google Calendar.

## Demo

You can watch a short demo of the voice agent interactions here:  
[Demo Video](https://drive.google.com/file/d/1xlL3eu-DVBb4I3VodigcVWrrrH53XBMx/view?usp=sharing)

## Setup

1. Clone the repository:

git clone https://github.com/rowanhossamm/voice-agent-llm.git
cd voice-agent-llm

2. Create a virtual environment and install dependencies:

``` bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

3. API Keys
For the agent to work with Google Calendar and Gemini LLM, you need to create your own API key.

A file named config.py is included as an example.

You can get your own API key here: [Google AI Studio API Keys](https://aistudio.google.com/api-keys)

Example config.py:

``` bash
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
``` 

Usage
Run the agent:

``` bash
python app.py
``` 

Speak commands like:

"List my appointments" → lists your upcoming events.

"Book an appointment" → the agent will ask for date and time.

Notes
The agent uses speech_recognition for speech-to-text and gTTS for text-to-speech.
