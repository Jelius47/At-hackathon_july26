import requests
from app.core.config import settings

def get_random_fact():
    url = "https://api.api-ninjas.com/v1/facts"
    headers = {"X-Api-Key": settings.API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()[0]["fact"]
    return "No fact available at the moment."
