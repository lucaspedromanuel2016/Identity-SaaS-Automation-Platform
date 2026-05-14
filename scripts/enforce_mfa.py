import os
import logging
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging configuration
logging.basicConfig(
    filename='logs/automation.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Environment variables
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

# Simulated user
USER_EMAIL = "lucas.manuel@example.com"

# MFA enforcement simulation
message = f"""
MFA SECURITY ENFORCEMENT

User: {USER_EMAIL}
Policy: MFA Required
Status: ENFORCED
"""

print(message)

logging.info(f"MFA enforced for {USER_EMAIL}")

# Send Slack security alert
payload = {
    "text": f"Security Alert: MFA enforced for {USER_EMAIL}"
}

response = requests.post(
    SLACK_WEBHOOK_URL,
    json=payload
)

print("Slack Status:", response.status_code)

if response.status_code == 200:
    print("Slack security alert sent.")
    logging.info("Slack MFA alert sent")

else:
    print("Slack notification failed.")
    logging.error(response.text)