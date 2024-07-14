import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import schedule
import time

# Email details
SMTP_SERVER = 'smtp.example.com'  # e.g., 'smtp.gmail.com' for Gmail
SMTP_PORT = 587
SMTP_USER = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
TO_EMAIL = 'recipient@example.com'
SUBJECT = 'Daily Report'

# Email content
def get_email_content():
    # Generate or read the content of the report
    # For demonstration, we'll use a simple text
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report_content = f'This is the daily report.\nGenerated on {current_time}'
    return report_content

# Function to send the email
def send_email():
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT

    # Attach the email body
    body = get_email_content()
    msg.attach(MIMEText(body, 'plain'))

    # Attach a file (if needed)
    # filename = 'report.pdf'
    # with open(filename, 'rb') as file:
    #     part = MIMEApplication(file.read(), Name=filename)
    #     part['Content-Disposition'] = f'attachment; filename="{filename}"'
    #     msg.attach(part)

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, TO_EMAIL, msg.as_string())
            print(f'Email sent successfully to {TO_EMAIL}')
    except Exception as e:
        print(f'Failed to send email: {e}')

# Schedule the email to be sent daily at a specific time
def schedule_daily_email():
    schedule.every().day.at("08:00").do(send_email)  # Schedule for 8 AM daily

    while True:
        schedule.run_pending()
        time.sleep(1)

# Main function
if __name__ == '__main__':
    schedule_daily_email()
