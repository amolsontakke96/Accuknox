import psutil
import logging
from datetime import datetime

CPU_THRESHOLD = 80      # CPU usage percent
MEM_THRESHOLD = 80      # Memory usage percent
DISK_THRESHOLD = 90     # Disk usage percent
MAX_PROCESSES = 300     # Maximum allowed processes
LOG_FILE = "/home/Amol/python/logs/system_health.log"  #Create a file on system and add the Log file path

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_alert(message):
    """Log alert to file and print to console."""
    print(message)
    logging.warning(message)

def check_cpu():
    """Check CPU usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"ALERT: CPU usage is high: {cpu_usage}%")

def check_memory():
    """Check memory usage."""
    mem = psutil.virtual_memory()
    if mem.percent > MEM_THRESHOLD:
        log_alert(f"ALERT: Memory usage is high: {mem.percent}%")

def check_disk():
    """Check disk usage for root partition."""
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        log_alert(f"ALERT: Disk usage is high: {disk.percent}%")

def check_processes():
    """Check number of running processes."""
    proc_count = len(psutil.pids())
    if proc_count > MAX_PROCESSES:
        log_alert(f"ALERT: Too many running processes: {proc_count}")

def monitor_system():
    """Run all health checks."""
    check_cpu()
    check_memory()
    check_disk()
    check_processes()

if __name__ == "__main__":
    monitor_system()
