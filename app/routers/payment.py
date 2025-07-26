# --- app/routers/payments.py ---
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from elusion.zenopay import ZenoPay
from elusion.zenopay.models import NewOrder
from elusion.zenopay.utils import generate_short_order_id
from app.schemas.payment import PaymentRequest, PaymentStatus
from app.models.models import Payment
from app.core.config import settings
from app.core.database import get_db

router = APIRouter()

@router.post("/payments/create", response_model=PaymentStatus)
def create_payment(request: PaymentRequest, db: Session = Depends(get_db)):
    client = ZenoPay(api_key=settings.ZENO_PAY_API)

    order = NewOrder(
        amount=request.amount,
        buyer_email=request.buyer_email,
        buyer_name=request.buyer_name,
        buyer_phone=request.buyer_phone,
        metadata=request.metadata,
        order_id=generate_short_order_id(prefix="ORDER", length=10),
        webhook_url="https://webhook.site/example-webhook-url"
    )

    res = client.orders.sync.create(order_data=order)

    new_payment = Payment(
        order_id=res.results.order_id,
        amount=request.amount,
        buyer_name=request.buyer_name,
        buyer_email=request.buyer_email,
        buyer_phone=request.buyer_phone,
        metadata=request.metadata,
        status="pending",
        paid=False
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return PaymentStatus(order_id=res.results.order_id, status="pending", paid=False)

@router.get("/payments/status/{order_id}", response_model=PaymentStatus)
def get_payment_status(order_id: str, db: Session = Depends(get_db)):
    client = ZenoPay(api_key=settings.ZENO_PAY_API)
    res = client.orders.sync.wait_for_payment(order_id=order_id)

    payment = db.query(Payment).filter(Payment.order_id == order_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    payment.status = res.results.status
    payment.paid = res.results.status == "paid"
    db.commit()

    return PaymentStatus(order_id=order_id, status=payment.status, paid=payment.paid)
