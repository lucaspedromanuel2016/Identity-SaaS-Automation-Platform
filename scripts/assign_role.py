import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    filename='logs/automation.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
AUTH0_ROLE_ID = os.getenv("AUTH0_ROLE_ID")
print("ROLE ID:", AUTH0_ROLE_ID)
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

# Get management token
token_response = requests.post(
    f"https://{AUTH0_DOMAIN}/oauth/token",
    json={
        "client_id": AUTH0_CLIENT_ID,
        "client_secret": AUTH0_CLIENT_SECRET,
        "audience": f"https://{AUTH0_DOMAIN}/api/v2/",
        "grant_type": "client_credentials"
    }
)

access_token = token_response.json()["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Replace with your Auth0 user ID
USER_ID = "auth0|6a0527e25e1fb984d6782292"

# Assign role
response = requests.post(
    f"https://{AUTH0_DOMAIN}/api/v2/users/{USER_ID}/roles",
    json={
        "roles": [AUTH0_ROLE_ID]
    },
    headers=headers
)

print("Status:", response.status_code)

if response.status_code == 204:
    print("Role assigned successfully")
    logging.info("Role assigned")

    requests.post(
        SLACK_WEBHOOK_URL,
        json={
            "text": "Auth0 RBAC role assigned successfully."
        }
    )

else:
    print(response.text)
    logging.error(response.text)