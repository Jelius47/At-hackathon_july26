import requests
from fastapi import FastAPI, Form
from fastapi.responses import Response
from typing import Optional
from dotenv import load_dotenv  # Import load_dotenv
import os  # Import os to access environment variables

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Fetch the API key from the environment variables
API_KEY = os.getenv("API_KEY")

def get_random_fact():
    """Fetches a random educational fact from API Ninjas."""
    url = f"https://api.api-ninjas.com/v1/facts"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        fact = response.json()[0]["fact"]  # Extract the first fact
        return fact
    else:
        return "Sorry, I couldn't retrieve a fact at the moment."

@app.post("/voicemail")
async def handle_call(
    isActive: str = Form(...),
    sessionId: str = Form(...),
    callerNumber: Optional[str] = Form(None),
    destinationNumber: Optional[str] = Form(None),
    direction: Optional[str] = Form(None),
    dtmfDigits: Optional[str] = Form(None),
    recordingUrl: Optional[str] = Form(None),
    durationInSeconds: Optional[str] = Form(None),
    currencyCode: Optional[str] = Form(None),
    amount: Optional[str] = Form(None),
):
    if isActive == "1":
        print("📞 Incoming call started")
        print(f"Session ID: {sessionId}")
        print(f"From: {callerNumber} ➡️ To: {destinationNumber}")
        print(f"Direction: {direction}")

        fact = get_random_fact()  # Fetch a fact
        
        xml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Say>Hello and welcome! I'm your AI learning assistant, here to help you discover new knowledge and sharpen your skills. Here is a single fact to keep you sharp. {fact}</Say>
        </Response>"""
        
        return Response(content=xml_response, media_type="application/xml")
    else:
        print("📞 Call ended")
        print(f"Session ID: {sessionId}")
        print(f"From: {callerNumber}")
        print(f"To: {destinationNumber}")
        print(f"Duration: {durationInSeconds} seconds")
        print(f"Currency: {currencyCode}")
        print(f"Amount: {amount}")
        print(f"Recording URL: {recordingUrl}")
        print(f"DTMF Input: {dtmfDigits}")

        return {"message": "Call session completed."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)