from django.contrib import admin

from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'price_usd', 'price_rub', 'delivery_dt', 'created_dt', 'updated_dt',
                    'expired_notification_sent')
    list_per_page = 25
