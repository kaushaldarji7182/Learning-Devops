import psutil
import time
from process_handler import handle_process

def monitor_cpu(threshold=20, interval=5):
    """
    Monitors CPU utilization and checks for high CPU-consuming processes.
    
    :param threshold: CPU usage percentage beyond which action is taken.
    :param interval: Time interval in seconds between checks.
    """
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage
        print(f"CPU Usage: {cpu_usage}%")
        
        if cpu_usage > threshold:
            print("High CPU Usage detected. Checking processes...")
            processes = [(p.pid, p.info['name'], p.info['cpu_percent'])
                         for p in psutil.process_iter(['name', 'cpu_percent'])
                         if p.info['cpu_percent']]
            
            for pid, name, cpu in sorted(processes, key=lambda x: x[2], reverse=True):
                if cpu > (threshold / 2):  # Consider processes consuming more than half the threshold
                    print(f"Process {name} (PID: {pid}) using {cpu}% CPU")
                    handle_process(pid, name)
        
        time.sleep(interval)  # Wait before next check
