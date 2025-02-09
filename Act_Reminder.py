from win10toast import ToastNotifier
from datetime import datetime, timezone, timedelta
from time import sleep

utc_dt = datetime.now(timezone.utc)
is_notification_sent = [0] * 24

toaster = ToastNotifier()

def send_reminder(msg):
    """Function to send a Windows notification."""
    toaster.show_toast("Urgent Reminder", msg, duration=5)

def schedule(date):
    """Schedule different reminders based on the time of day."""
    hour = date.hour

    # Lunch and water reminder at 1 PM
    if hour == 13 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("It's time for lunch and water!!")

    # Snacks reminder at 4 PM
    if hour == 16 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("It's time for snacks and water!!")

    # Log off reminder at 6 PM
    if hour == 18 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("It's time to log off from work!!")

    # Water reminders every hour from 9 AM to 6 PM (except 1 PM & 4 PM)
    for i in range(9, 18):
        if hour == i and hour not in [13, 16] and is_notification_sent[hour] == 0:
            is_notification_sent[hour] = 1
            send_reminder("It's time to drink water!!")

if __name__ == "__main__":
    prev_date = utc_dt.astimezone() - timedelta(days=1)
    while True:
        date = datetime.now().astimezone()
        
        # Reset the notification list at the start of a new day
        if date.day == 1 or date.day > prev_date.day:
            is_notification_sent = [0] * 24
            prev_date = date

        schedule(date)
        sleep(300)  # Wait 5 minutes before checking again
