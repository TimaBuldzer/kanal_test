from django.db import models


class Order(models.Model):
    external_id = models.BigIntegerField(unique=True, verbose_name='External ID')
    price_usd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price USD')
    price_rub = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price RUB')
    delivery_dt = models.DateField(verbose_name='Delivery date')

    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated_dt = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    expired_notification_sent = models.BooleanField(default=False, verbose_name='Expired notification sent')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_dt']

    def __str__(self):
        return f'Order {self.external_id}'
