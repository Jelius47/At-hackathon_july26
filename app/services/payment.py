from elusion.zenopay import ZenoPay
from elusion.zenopay.models import NewOrder
from elusion.zenopay.utils import generate_short_order_id
from app.core.config import settings
from typing import Optional

client = ZenoPay(api_key=settings.ZENO_PAY_API)

def create_order(
    amount: float,
    buyer_name: str,
    buyer_email: str,
    buyer_phone: str,
    metadata: Optional[dict] = None
):
    order = NewOrder(
        amount=amount,
        buyer_email=buyer_email,
        buyer_name=buyer_name,
        buyer_phone=buyer_phone,
        metadata=metadata,
        order_id=generate_short_order_id(prefix="ORDER", length=10),
        webhook_url=settings.ZENO_PAY_WEBHOOK
    )
    return client.orders.sync.create(order_data=order)

def wait_for_payment(order_id: str):
    return client.orders.sync.wait_for_payment(order_id=order_id)
