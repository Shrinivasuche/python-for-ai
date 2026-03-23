import os

import requests
from dotenv import load_dotenv

# Basic Python script to demonstrate API calls
response = requests.get("https://api.github.com")
print(response.status_code)


# setting environment variables
load_dotenv()

api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_URL")
