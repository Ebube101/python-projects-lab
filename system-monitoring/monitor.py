import psutil
import time
from datetime import datetime

# Log file to store system usage
LOG_FILE = "system_usage.log"

def log_system_usage():
    """Logs CPU and memory usage to the console and a file."""
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage
        memory_usage = psutil.virtual_memory().percent  # Get memory usage

        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%"
        print(log_entry)  # Print to console

        # Append log to file
        with open(LOG_FILE, "a") as log_file:
            log_file.write(log_entry + "\n")

        time.sleep(5)  # Wait 5 seconds before next update

if __name__ == "__main__":
    log_system_usage()
