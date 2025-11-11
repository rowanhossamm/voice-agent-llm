import google.generativeai as genai
import os
import json
import re
from datetime import datetime

import os
import google.generativeai as genai
from config import GOOGLE_API_KEY

api_key = GOOGLE_API_KEY

genai.configure(api_key=api_key)

MODEL_NAME = "models/gemini-2.0-flash"

SYSTEM_PROMPT = """
You ONLY output a JSON object. No text, no explanations, no greetings.

FORMAT (always):
{
  "intent": "list_appointments" | "book_appointment" | "unknown",
  "date": "YYYY-MM-DD or null",
  "time": "HH:MM or null"
}

RULES:
1. If the user says: list, show, check, schedule, appointments → "list_appointments"
2. If user gives BOTH a date AND time → "book_appointment"
3. If only date OR only time → "unknown"
4. If unclear → "unknown"
5. NO other words allowed. NO greetings. NO sentences.
"""


def parse_with_llm(user_text):
    text = user_text.lower().strip()
    date = None
    time = None

    # Detect date (simple patterns)
    month_map = {
        "january":"01", "february":"02", "march":"03", "april":"04",
        "may":"05", "june":"06", "july":"07", "august":"08",
        "september":"09", "october":"10", "november":"11", "december":"12"
    }

    # Match patterns like "12 November 2025" or "November 12 2025"
    date_match = re.search(r'(\d{1,2})\s+([a-zA-Z]+)(\s+(\d{4}))?', text)
    if not date_match:
        date_match = re.search(r'([a-zA-Z]+)\s+(\d{1,2})(\s+(\d{4}))?', text)

    if date_match:
        day = date_match.group(1 if date_match.group(1).isdigit() else 2)
        month_name = date_match.group(2 if date_match.group(1).isdigit() else 1).lower()
        year = date_match.group(4) if date_match.group(4) else str(datetime.now().year)
        if month_name in month_map:
            date = f"{year}-{month_map[month_name]}-{int(day):02d}"

    # Detect time (HH:MM)
    time_match = re.search(r'(\d{1,2}:\d{2})', text)
    if time_match:
        time = time_match.group(1)
    
    # Determine intent
    intent = "unknown"
    if "list" in text:
        intent = "list_appointments"
    elif "book" in text or "schedule" in text or date or time:
        intent = "book_appointment"

    return {"intent": intent, "date": date, "time": time}
