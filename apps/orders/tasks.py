from conf.celery import app
from apps.orders.logics import OrderLogic


@app.task
def create_orders() -> None:
    logics = OrderLogic()
    logics.create_orders()
