from __future__ import print_function
import datetime
import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None

    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def list_events():
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'

    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()

    return events_result.get('items', [])


def book_event(date, time, summary="Appointment"):
    service = get_calendar_service()

    start_dt = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    start_dt = start_dt.replace(tzinfo=ZoneInfo("Africa/Cairo"))
    end_dt = start_dt + timedelta(hours=1)
    start = start_dt.isoformat()
    end = end_dt.isoformat()


    event = {
        'summary': summary,
        'start': {
            'dateTime': start_dt.isoformat(),
            'timeZone': 'Africa/Cairo',
        },
        'end': {
            'dateTime': end_dt.isoformat(),
            'timeZone': 'Africa/Cairo',
        }
    }
    event_result = service.events().insert(calendarId='primary', body=event).execute()

    return event_result
