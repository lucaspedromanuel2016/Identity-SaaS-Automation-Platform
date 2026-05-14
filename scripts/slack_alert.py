import os
import logging
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    filename='logs/automation.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Read webhook URL
webhook_url = os.getenv("SLACK_WEBHOOK_URL")

# Validate webhook URL
if not webhook_url:
    logging.error("SLACK_WEBHOOK_URL missing from .env")
    raise ValueError("SLACK_WEBHOOK_URL not found")

# Slack message payload
payload = {
    "text": "IAM Automation Platform is working."
}

try:
    # Send Slack notification
    response = requests.post(webhook_url, json=payload)

    # Success logging
    if response.status_code == 200:
        print("Slack notification sent successfully.")
        logging.info("Slack notification sent successfully.")

    else:
        print("Failed to send Slack notification.")
        logging.error(f"Slack API error: {response.text}")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
    logging.error(f"Request exception: {e}")