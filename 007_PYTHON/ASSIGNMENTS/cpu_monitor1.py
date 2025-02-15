import psutil
import smtplib
import os
import time
from email.message import EmailMessage

# Configuration
CPU_THRESHOLD = 60  # Overall CPU usage threshold
PROCESS_THRESHOLD = 10  # Individual process CPU threshold
EMAIL_RECEIVER = "kaushaldarji7182@gmail.com"  # Replace with your email
EMAIL_SENDER = "kaushaldarji7182@gmail.com"  # Replace with SMTP sender email
EMAIL_PASSWORD = "your-email-password"  # Replace with SMTP password (Use environment variable for security)

# Function to send email alert
def send_email(process_name, pid, cpu_usage):
    msg = EmailMessage()
    msg["Subject"] = "⚠ High CPU System Process Alert"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg.set_content(f"High CPU usage detected!\n\nProcess: {process_name}\nPID: {pid}\nCPU Usage: {cpu_usage:.2f}%")

    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"📩 Email sent for system process {process_name} (PID: {pid})")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Function to restart a process
def restart_process(pid):
    try:
        process = psutil.Process(pid)
        process_name = process.name()
        print(f"🔄 Restarting application process: {process_name} (PID: {pid})")
        process.terminate()
        time.sleep(2)  # Give time to terminate
        os.system(f"{process_name} &")  # Restart process
    except Exception as e:
        print(f"❌ Error restarting process {pid}: {e}")

# Function to kill a process
def kill_process(pid):
    try:
        process = psutil.Process(pid)
        print(f"❌ Killing process: {process.name()} (PID: {pid})")
        process.terminate()
    except Exception as e:
        print(f"❌ Error killing process {pid}: {e}")

# Monitoring Function
def monitor_cpu():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        
        if cpu_usage > CPU_THRESHOLD:
            print(f"⚠ High CPU detected: {cpu_usage:.2f}%")

            # Get processes consuming high CPU
            for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
                try:
                    process_info = proc.info
                    pid = process_info['pid']
                    process_name = process_info['name']
                    process_cpu = process_info['cpu_percent']

                    if process_cpu > PROCESS_THRESHOLD:
                        print(f"🔍 High CPU Process: {process_name} (PID: {pid}) - {process_cpu:.2f}%")

                        # Check if it's a system process
                        if pid < 1000:  # System processes usually have low PIDs
                            send_email(process_name, pid, process_cpu)
                        elif "chrome" in process_name.lower() or "python" in process_name.lower():  # Example: Application processes
                            restart_process(pid)
                        else:
                            kill_process(pid)

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
        
        time.sleep(5)  # Check every 5 seconds

# Run the monitoring function
if __name__ == "__main__":
    monitor_cpu()
