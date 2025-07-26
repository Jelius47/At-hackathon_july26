from fastapi import FastAPI, Form
from fastapi.responses import Response
from typing import Optional
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/audio", StaticFiles(directory="audio"), name="audio")

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

        # Respond with instructions — you can customize this part
        xml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>Hello and welcome! I'm your AI learning assistant, here to help you discover new knowledge and sharpen your skills. Here's a fact for you. There are more than 1,100 known tributaries flowing into the Amazon River. Tributaries are sources of water such as a small river, stream  or other water flow that reaches the river.</Say>
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

        return {
            "message": "Call session completed.",
            "sessionId": sessionId,
            "duration": durationInSeconds,
            "currency": currencyCode,
            "amount": amount,
            "recording": recordingUrl,
            "dtmf": dtmfDigits,
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
