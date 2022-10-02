from typing import List

from django.db import transaction

from apps.google_api.services import SpreadSheetParser
from apps.orders.models import Order


@transaction.atomic
def create_orders() -> None:
    parser = SpreadSheetParser()
    orders_data = parser.get_orders_data()

    orders_to_create: List[Order] = list()
    for order_data in orders_data:
        orders_to_create.append(Order(**order_data.dict()))

    Order.objects.all().delete()
    Order.objects.bulk_create(orders_to_create)
