# --- app/routers/payments.py ---
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.payment import PaymentRequest, PaymentStatus
from app.models.models import Payment
from app.core.config import settings
from app.core.database import get_db
from app.services.payment import create_zenopay_order, get_zenopay_payment_status

router = APIRouter()

@router.post("/payments/create", response_model=PaymentStatus)
def create_payment(request: PaymentRequest, db: Session = Depends(get_db)):
    order_response = create_zenopay_order(request)

    new_payment = Payment(
        order_id=order_response.results.order_id,
        amount=request.amount,
        buyer_name=request.buyer_name,
        buyer_email=request.buyer_email,
        buyer_phone=request.buyer_phone,
        extra_data=request.extra_data,
        status="pending",
        paid=False
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return PaymentStatus(order_id=new_payment.order_id, status="pending", paid=False)

@router.get("/payments/status/{order_id}", response_model=PaymentStatus)
def get_payment_status(order_id: str, db: Session = Depends(get_db)):
    status_response = get_zenopay_payment_status(order_id)

    payment = db.query(Payment).filter(Payment.order_id == order_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    payment.status = status_response.results.status
    payment.paid = status_response.results.status == "paid"
    db.commit()

    return PaymentStatus(order_id=order_id, status=payment.status, paid=payment.paid)
