import requests
from ics import Calendar
from datetime import datetime
import pytz
import os

ICS_URL = os.environ.get('CANVAS_URL')
topic = os.environ.get('NTFY_TOPIC')

response = requests.get(ICS_URL)
calendar = Calendar(response.text)

local_tz = pytz.timezone("America/Los_Angeles")
now = datetime.now(local_tz)
message = ""
importantMessage = ""

for event in sorted(calendar.events, key=lambda e: e.begin):
    due = event.end.astimezone(local_tz)
    
    if due.date() == now.date(): 
        importantMessage += f"{event.name}\nDue: {due.strftime('%Y-%m-%d %I:%M %p')}\n" + "-"*30 + "\n"
    elif due > now:
        message += f"{event.name}\nDue: {due.strftime('%Y-%m-%d %I:%M %p')}\n" + "-"*30 + "\n" 
        # print(message)


if message:
    print(message)
    requests.post(
        f"https://ntfy.sh/{topic}",
        data=message
    )
if importantMessage:
    print("IMPORTANT DUE TODAY | IMPORTANT DUE TODAY | IMPORTANT DUE TODAY")
    print(importantMessage) 
    prefix = "IMPORTANT DUE TODAY | IMPORTANT DUE TODAY | IMPORTANT DUE TODAY\n"
    toSend = prefix + importantMessage

    requests.post(
        f"https://ntfy.sh/{topic}",
        data=toSend
    )
