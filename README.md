💡  **Reminder Notification Script**

While working on our laptops, we usually don't keep an eye on time. 
We barely get up and drink water, have lunch/snacks proper on time and tend to miss it. On a serious note, it affects our health in so many bad ways!
There exists a cool technical solution to this problem:
And that is to create an application which will remind us of important activities like drinking water, having lunch, snacks etc by sending notifications on the laptop. Hence, I tried implementing it.

**So, Let's run the code**

This Python script sends desktop notifications at specific times during the day to remind you about:

✅ Lunch & Water (1 PM)

✅ Snacks & Water (4 PM)

✅ Logging Off (6 PM)

✅ Drinking Water (Every hour from 9 AM - 6 PM, except 1 PM & 4 PM)

It runs in the background and checks every 5 minutes to send reminders.

**📌 Features**

Sends notifications using Windows 10/11’s built-in notification system (win10toast).

Automatically resets reminders at the start of a new day.

Ensures no duplicate notifications within the same hour.

Lightweight & runs silently in the background.

**🛠️ Installation & Setup**

1️⃣ Install Python

Check if Python is installed by running:

python --version

If not installed, download it from Python.org and check "Add Python to PATH" during installation.

**2️⃣ Install Required Libraries**

Open Command Prompt (CMD) and run:

**pip install win10toast**

🚀 How to Run
Save the script as reminder.py

Open Command Prompt (CMD)

Navigate to the script’s folder:

cd path\to\your\script
(Example: cd C:\Users\YourName\Documents)

**Run the script:**


python reminder.py
The script will start running in the background and send notifications at the scheduled times.

**📜 Code Explanation**

Uses win10toast to send Windows notifications.
Runs an infinite loop to check the time every 5 minutes (sleep(300)).
Sends reminders for lunch, snacks, logging off, and drinking water.
Prevents duplicate notifications by tracking already sent reminders.
Resets notifications at midnight for the next day.

🎯 Example Notifications

🔔 "It's time for lunch and water!!" (1 PM)

🔔 "It's time for snacks and water!!" (4 PM)

🔔 "It's time to log off from work!!" (6 PM)

🔔 "It's time to drink water!!" (Every hour between 9 AM - 6 PM, except 1 PM & 4 PM)

💡 Customization

### You can modify the script to:

Change notification times (edit schedule() function).
Add more reminders (e.g., exercise, meetings, etc.).
Adjust notification frequency (change sleep(300) to a different interval).
