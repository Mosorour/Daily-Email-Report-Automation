# Daily-Email-Report-Automation

This project contains a Python script that automates sending daily email reports. It uses the `smtplib` library for sending emails and `schedule` library for scheduling the daily email tasks.

## Prerequisites

- Python 3.x
- Required libraries:
  - `smtplib`
  - `email`
  - `schedule`

You can install the required libraries using pip:

```
pip install schedule
```

## Setup

1- Clone the repository or download the script file daily_report_email.py.

2- Update the script with your email details:
```
SMTP_SERVER = 'smtp.example.com'  # e.g., 'smtp.gmail.com' for Gmail
SMTP_PORT = 587
SMTP_USER = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
TO_EMAIL = 'recipient@example.com'
SUBJECT = 'Daily Report'
```

Alternatively, you can use environment variables to avoid hardcoding sensitive information:
```
import os

SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.example.com')
SMTP_PORT = os.getenv('SMTP_PORT', 587)
```
Then, set the environment variables in your operating system or in a .env file if you're using tools like python-dotenv.

3- Customize the email content by modifying the get_email_content function:
```
def get_email_content():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report_content = f'This is the daily report.\nGenerated on {current_time}'
    return report_content
```

4-(Optional) If you need to attach files to the email, uncomment and modify the file attachment section:
```
# Attach a file (if needed)
# filename = 'report.pdf'
# with open(filename, 'rb') as file:
#     part = MIMEApplication(file.read(), Name=filename)
#     part['Content-Disposition'] = f'attachment; filename="{filename}"'
#     msg.attach(part)
```

## Running the Script

To run the script manually, execute:

```
python daily_report_email.py
```

## Scheduling the Script

To ensure the script runs daily without manual intervention, you can use a task scheduler like cron on Linux or Task Scheduler on Windows.

### Linux (using cron)
1- Open the crontab editor:
```
crontab -e
```
2- Add the following line to schedule the script to run daily at 8 AM:
```
0 8 * * * /usr/bin/python3 /path/to/daily_report_email.py
```
### Windows (using Task Scheduler)
1- Open Task Scheduler.
2- Create a new task.
3- Set the trigger to daily at your desired time.
4- Set the action to start a program, and provide the path to the Python executable and the script file.
