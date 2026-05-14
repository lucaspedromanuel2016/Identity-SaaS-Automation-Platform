import os
from dotenv import load_dotenv

load_dotenv()

print("Domain:", os.getenv("AUTH0_DOMAIN"))
print("Client ID:", os.getenv("AUTH0_CLIENT_ID"))