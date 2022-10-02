from conf.celery import app
from apps.orders import logics


@app.task
def create_orders() -> None:
    logics.create_orders()
