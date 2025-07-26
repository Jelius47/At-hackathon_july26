from fastapi import APIRouter, Form
from fastapi.responses import Response
from typing import Optional
from app.services.facts import get_random_fact

router = APIRouter()

@router.post("/voicemail")
async def handle_voicemail(
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
        fact = get_random_fact()
        xml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Say>Hello! Here’s a fact to keep you sharp: {fact}</Say>
        </Response>"""
        return Response(content=xml_response, media_type="application/xml")
    else:
        return {"message": "Call session completed."}
