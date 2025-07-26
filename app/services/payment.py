from elusion.zenopay import ZenoPay
from elusion.zenopay.models import NewOrder
from elusion.zenopay.utils import generate_short_order_id
from app.core.config import settings

order = NewOrder(
    amount=200,
    buyer_email="maverickweyunga@gmail.com",
    buyer_name="maveric",
    buyer_phone="255763848561",
    metadata={"key": "value"},
    order_id=generate_short_order_id(prefix="ORDER", length=10),
    webhook_url="https://webhook.site/1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
)

client = ZenoPay(
    api_key=settings.ZENO_PAY_API,
)

res = client.orders.sync.create(order_data=order)

print("=====================\n")
print(res.results)
print("=====================\n")
print(res.results.order_id)
print("=====================\n")

res2 = client.orders.sync.wait_for_payment(order_id=res.results.order_id)
print("Wait for payment\n")
print(res2.results)