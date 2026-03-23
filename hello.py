# Basic Python script to demonstrate API calls
import requests

response = requests.get('https://api.github.com')
print(response.status_code)


# setting environment variables
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

#Read from environment 
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_URL')