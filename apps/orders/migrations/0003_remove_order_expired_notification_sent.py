# Generated by Django 4.1.1 on 2022-10-02 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_expired_notification_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='expired_notification_sent',
        ),
    ]