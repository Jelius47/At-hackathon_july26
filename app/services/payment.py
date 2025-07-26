# app/services/payment.py

from elusion.zenopay import ZenoPay
from elusion.zenopay.models import NewOrder
from elusion.zenopay.utils import generate_short_order_id
from app.core.config import settings
from typing import Optional

client = ZenoPay(api_key=settings.ZENO_PAY_API)

def create_zenopay_order(  # ✅ Renamed to match import
    amount: float,
    buyer_name: str,
    buyer_email: str,
    buyer_phone: str,
    extra_data: Optional[dict] = None
):
    order = NewOrder(
        amount=amount,
        buyer_email=buyer_email,
        buyer_name=buyer_name,
        buyer_phone=buyer_phone,
        metadata=extra_data or {},
        order_id=generate_short_order_id(prefix="ORDER", length=10),
        webhook_url=settings.ZENO_PAY_WEBHOOK
    )
    return client.orders.sync.create(order_data=order)

def get_zenopay_payment_status(order_id: str):  # ✅ Renamed to match import
    return client.orders.sync.wait_for_payment(order_id=order_id)
