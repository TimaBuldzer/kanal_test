from typing import List
import datetime
from django.db import transaction

from apps.google_api.services import SpreadSheetParser, OrderData
from apps.orders.models import Order
from apps.telegram.services import TelegramBot
from apps.users.models import User


class OrderLogic:

    @transaction.atomic
    def create_orders(self) -> None:
        parser = SpreadSheetParser()
        orders_data = parser.get_orders_data()
        orders_to_create: List[Order] = list()
        for order_data in orders_data:
            self.__send_message_about_order_expire(order_data)
            orders_to_create.append(Order(**order_data.dict()))

        Order.objects.all().delete()
        Order.objects.bulk_create(orders_to_create)

    @staticmethod
    def __send_message_about_order_expire(order_data: OrderData) -> None:
        now = datetime.datetime.now().date()
        if order_data.delivery_dt > now:
            return
        for user in User.objects.filter(is_superuser=True):
            bot = TelegramBot()
            bot.send_message(user.tg_id, f'Order {order_data.external_id} delivery time has expired')
