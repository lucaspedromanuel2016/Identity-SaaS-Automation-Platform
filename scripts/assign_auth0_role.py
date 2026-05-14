import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Env vars
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
ROLE_ID = os.getenv("AUTH0_EMPLOYEE_ROLE_ID")

if not all([AUTH0_DOMAIN, AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, ROLE_ID]):
    raise ValueError("Missing required environment variables")

# ---- Step 1: Get Management API token ----
token_url = f"https://{AUTH0_DOMAIN}/oauth/token"

token_payload = {
    "client_id": AUTH0_CLIENT_ID,
    "client_secret": AUTH0_CLIENT_SECRET,
    "audience": f"https://{AUTH0_DOMAIN}/api/v2/",
    "grant_type": "client_credentials"
}

token_response = requests.post(token_url, json=token_payload)
token_response.raise_for_status()

access_token = token_response.json()["access_token"]
print("Access token acquired.")

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# ---- Step 2: Find user by email ----
user_email = "lucas.manuel@example.com"

search_url = f"https://{AUTH0_DOMAIN}/api/v2/users-by-email"
search_response = requests.get(
    search_url,
    headers=headers,
    params={"email": user_email}
)
search_response.raise_for_status()

users = search_response.json()

if not users:
    raise ValueError(f"User not found: {user_email}")

user_id = users[0]["user_id"]
print("Found user:", user_id)

# ---- Step 3: Assign role ----
assign_url = f"https://{AUTH0_DOMAIN}/api/v2/users/{user_id}/roles"

payload = {
    "roles": [ROLE_ID]
}

assign_response = requests.post(
    assign_url,
    headers=headers,
    json=payload
)

print("Status Code:", assign_response.status_code)
print("Response:", assign_response.text)

if assign_response.status_code == 204:
    print("Role assigned successfully.")
else:
    print("Role assignment failed.")