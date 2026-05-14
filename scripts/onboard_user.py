import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read Slack webhook URL correctly
slack_webhook = os.getenv("SLACK_WEBHOOK_URL")

# Debug check
print("Webhook:", slack_webhook)

# Validate webhook
if not slack_webhook:
    raise ValueError("SLACK_WEBHOOK_URL not found")

# Slack payload
payload = {
    "text": "New Auth0 user onboarding completed successfully."
}

# Send Slack notification
response = requests.post(slack_webhook, json=payload)

# Output result
print("Status Code:", response.status_code)
print("Response:", response.text)