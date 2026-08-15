"""
Problem #28: Send Email via Gmail using SMTP
Date: 2026-08-16

A simple script to send an email using Gmail's SMTP server.
Uses App Password for authentication (regular passwords are not accepted by Google).
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = ""          
receiver_email = ""        
app_password = ""          

# Create email content
subject = "Test email"
body = "This is a test email sent from a Python script."

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))


def send_email():
    """Send the email using Gmail's SMTP server."""
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Enable TLS encryption
            server.login(sender_email, app_password)
            server.send_message(message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    send_email()
