import os
import smtplib
from email.message import EmailMessage

EMAIL_SENDER = "kaushaldarji7182@gmail.com"
EMAIL_PASSWORD = os.getenv("SMTP_PASSWORD")  # App password
EMAIL_RECEIVER = "kaushaldarji7182@gmail.com"

def send_email():
    if not EMAIL_PASSWORD:
        print("❌ SMTP password not found. Set the environment variable 'SMTP_PASSWORD'.")
        return
    
    msg = EmailMessage()
    msg["Subject"] = "Test Email"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg.set_content("This is a test email.")

    try:
        print("🔄 Connecting to Gmail SMTP server...")
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

send_email()
