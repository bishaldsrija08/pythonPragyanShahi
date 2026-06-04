from datetime import datetime

# Events
events = {
    "project deadline": "2026-05-31",
    "team meeting": "2026-06-01",
    "exam": "2026-06-15",
    "birthday": "2025-07-21",
}

# today
today = datetime.now().date()

for event, date in events.items():
    event_date = datetime.strptime(date, "%Y-%m-%d").date()
    remaining_days = (event_date - today).days
    if remaining_days > 0:
        print(f"{event} is in {remaining_days} days.")
    elif remaining_days == 0:
        print(f"{event} is today!")
    else:
        print(f"{event} has already passed.")