import smtplib
from email.mime.text import MIMEText

def send_email(process_name, pid):
    """
    Sends an email alert for a high CPU-consuming system process.
    
    :param process_name: Name of the process.
    :param pid: Process ID.
    """
    sender_email = "kaushaldarji7182@gmail.com"
    recipient_email = "kaushaldarji7182@gmail.com"
    subject = f"High CPU Usage Alert: {process_name}"
    body = f"The system process '{process_name}' (PID: {pid}) is consuming high CPU."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("your_email@example.com", "your_password")
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email alert sent for process {process_name} (PID: {pid}).")
    except Exception as e:
        print(f"Failed to send email: {e}")
