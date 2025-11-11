from speech_to_text import voice_to_text
from text_to_speech import speak
from llm_engine import parse_with_llm
from calendar_api import list_events, book_event
from datetime import datetime

from datetime import datetime

from datetime import datetime

# Keep track of last partial info
last_date = None
last_time = None

def handle_intent():
    global last_date, last_time

    text = voice_to_text()
    if not text or len(text.strip()) < 3:
        return

    data = parse_with_llm(text)
    intent = data.get("intent")
    date = data.get("date")
    time = data.get("time")

    
    # Update last known values
    if date:
        last_date = date
    elif not date and last_date:
        date = last_date

    if time:
        last_time = time
    elif not time and last_time:
        time = last_time

    # Handle listing appointments
    if intent == "list_appointments":
        events = list_events()
        if not events:
            speak("You have no upcoming events.")
            return

        # Remove duplicates
        seen = set()
        filtered_events = []
        for e in events:
            key = (e.get('summary'), e['start'].get('dateTime', e['start'].get('date')))
            if key not in seen:
                filtered_events.append(e)
                seen.add(key)
        events = filtered_events[:5]  # read top 5 only

        # Build message
        message = "Your upcoming events are: "
        for event in events:
            start_info = event['start']
            if 'dateTime' in start_info:
                start_dt = datetime.fromisoformat(start_info['dateTime'])
                start_str = start_dt.strftime("%b %d at %H:%M")
            elif 'date' in start_info:
                start_dt = datetime.fromisoformat(start_info['date'])
                start_str = start_dt.strftime("%b %d (All day)")
            else:
                start_str = "Unknown time"

            summary = event.get('summary', 'No title')
            message += f"{summary} at {start_str}. "

        speak(message)

    # Handle booking appointments
    elif intent == "book_appointment":
        if not date and not time:
            speak("Do you want to book an appointment? Please tell me the date and time.")
            return
        elif not date:
            speak("I got the time. Please tell me the date for the appointment.")
            return
        elif not time:
            speak("I got the date. Please tell me the time for the appointment.")
            return

        # Both date and time are present → book
        event = book_event(date, time)
        speak(f"Your appointment has been booked on {date} at {time}.")
        # Reset last known info after booking
        last_date = None
        last_time = None

    # Unknown intent but partial info exists
    else:
        if date and not time:
            speak("I got the date. Please tell me the time for the appointment.")
        elif time and not date:
            speak("I got the time. Please tell me the date for the appointment.")
        else:
            speak("I’m not sure what you want. Do you want to book an appointment or list your events?")



if __name__ == "__main__":
    try:
        while True:
            input("Press Enter to speak...")
            handle_intent()
    except KeyboardInterrupt:
        print("Exiting...")

