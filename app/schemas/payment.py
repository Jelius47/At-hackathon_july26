# --- app/schemas/payment.py ---
from pydantic import BaseModel, EmailStr
from typing import Optional

class PaymentRequest(BaseModel):
    amount: float
    buyer_name: str
    buyer_email: Optional[str] = None
    buyer_phone: str
    metadata: Optional[dict] = None

class PaymentStatus(BaseModel):
    order_id: str
    status: str
    paid: bool