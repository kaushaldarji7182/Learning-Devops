import psutil
import os
import signal
from email_alert import send_email

def is_system_process(pid):
    """
    Determines if the given process is a system process.
    
    :param pid: Process ID.
    :return: True if it's a system process, False otherwise.
    """
    try:
        process = psutil.Process(pid)
        return process.username() == 'root'  # Assuming system processes run as root
    except psutil.NoSuchProcess:
        return False

def restart_process(pid, name):
    """
    Restarts an application process.
    
    :param pid: Process ID.
    :param name: Process Name.
    """
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Restarting process {name} (PID: {pid})...")
        process.wait()
        os.system(f"{name} &")  # Restarting process
    except Exception as e:
        print(f"Failed to restart process {name}: {e}")


def kill_process(pid, name):
    """
    Kills an unknown process.

    :param pid: Process ID.
    :param name: Process Name.
    """
    try:
        process = psutil.Process(pid)
        process.terminate()  # First attempt a graceful shutdown
        process.wait(timeout=5)  # Wait for it to exit

        if process.is_running():  # If it's still running, force kill it
            process.kill()
            print(f"Process {name} (PID: {pid}) forcefully killed.")
        else:
            print(f"Process {name} (PID: {pid}) terminated successfully.")

    except psutil.NoSuchProcess:
        print(f"Process {name} (PID: {pid}) does not exist.")
    except psutil.AccessDenied:
        print(f"Permission denied to terminate {name} (PID: {pid}). Try running as Administrator.")
    except Exception as e:
        print(f"Failed to kill process {name}: {e}")


def handle_process(pid, name):
    """
    Handles a high CPU-consuming process based on its type.
    
    :param pid: Process ID.
    :param name: Process Name.
    """
    if is_system_process(pid):
        send_email(name, pid)
    elif name in ["your_application"]:  # Replace with actual application names
        restart_process(pid, name)
    else:
        kill_process(pid, name)
