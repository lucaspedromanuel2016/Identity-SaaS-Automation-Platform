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

# Environment variables
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")

# Validate variables
if not AUTH0_DOMAIN or not AUTH0_CLIENT_ID or not AUTH0_CLIENT_SECRET:
    raise ValueError("Missing Auth0 environment variables")

# Step 1: Get Management API Token
token_url = f"https://{AUTH0_DOMAIN}/oauth/token"

token_payload = {
    "client_id": AUTH0_CLIENT_ID,
    "client_secret": AUTH0_CLIENT_SECRET,
    "audience": f"https://{AUTH0_DOMAIN}/api/v2/",
    "grant_type": "client_credentials"
}

token_response = requests.post(token_url, json=token_payload)

if token_response.status_code != 200:
    print("Failed to get access token")
    print(token_response.text)
    exit()

access_token = token_response.json()["access_token"]

print("Access token acquired.")

# Step 2: Create User
create_user_url = f"https://{AUTH0_DOMAIN}/api/v2/users"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

user_payload = {
    "email": "lucas.manuel@example.com",
    "password": "StrongPassword123!",
    "connection": "Username-Password-Authentication",
    "given_name": "Lucas",
    "family_name": "Manuel",
    "name": "Lucas Manuel"
}

response = requests.post(
    create_user_url,
    json=user_payload,
    headers=headers
)

print("Status Code:", response.status_code)
print(response.text)

if response.status_code in [200, 201]:
    print("User created successfully.")
    logging.info("Auth0 user created successfully")

else:
    print("Failed to create user.")
    logging.error(f"Auth0 API error: {response.text}")