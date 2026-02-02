# canvas-daily-tracker

A simple Python script that fetches assignment due dates from a Canvas calendar feed and displays upcoming or due-today assignments. It works well on a Raspberry Pi or any system running Python and can be automated with cron to send reminders or notifications.

## Features
- Fetches assignments from Canvas calendar feed (ICS)
- Shows assignments due today
- Lists upcoming assignments
- Converts times to local timezone
- Can run automatically with cron
- Easy to extend with SMS/email notifications

## Requirements
Python 3.9+ recommended.

Install required packages:

```bash
pip install requests ics pytz
```

### Raspberry Pi OS Note
If you get an "externally-managed-environment" error:

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests ics pytz
```

## Setup

### 1. Get Canvas Calendar Feed
In Canvas:
1. Open **Calendar**
2. Click **Calendar Feed**
3. Copy the ICS URL

### 2. Update Script
Open `canvas.py` and replace:

```python
ICS_URL = "YOUR_URL_HERE"
```

with your Canvas calendar feed link.

## Running the Script

Run manually:

```bash
python canvas.py
```

The script prints assignments due today and upcoming deadlines.

## Automating with Cron

Example: run every hour.

Open cron editor:

```bash
crontab -e
```

Add this line (update paths):

```bash
0 * * * * /usr/bin/python3 /path/to/canvas.py >> /path/to/log.txt 2>&1
```

## Example Output

```
Assignment 3
Due: 2026-02-01 11:59 PM
------------------------------
Homework 4
Due: 2026-02-03 11:59 PM
```

## Possible Improvements
- SMS notifications
- Email reminders
- Discord/Slack alerts
- Daily summaries
- Web dashboard
- Priority sorting

## Author
Leonardo Gamboa  
Cal Poly Pomona – Computer Science
