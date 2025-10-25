import requests
import logging
import os
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------
APP_URL = "https://wisecow.local:32677/"  # Replace with your application URL
LOG_DIR = "/home/Amol/python/logs" # Directory to store log files
LOG_FILE = os.path.join(LOG_DIR, "application_health.log")
TIMEOUT = 5  # seconds

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_application(url):
    """Check if the application is up by sending an HTTP GET request."""
    try:
        response = requests.get(url, timeout=TIMEOUT, verify=False)
        if 200 <= response.status_code < 300:
            message = f"UP: Application is functioning correctly (Status Code: {response.status_code})"
            print(message)
            logging.info(message)
        else:
            message = f"DOWN: Application returned an unexpected status code {response.status_code}"
            print(message)
            logging.warning(message)
    except requests.exceptions.RequestException as e:
        message = f"DOWN: Application is unreachable ({e})"
        print(message)
        logging.warning(message)

if __name__ == "__main__":
    check_application(APP_URL)
