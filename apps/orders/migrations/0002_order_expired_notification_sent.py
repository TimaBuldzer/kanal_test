# Generated by Django 4.1.1 on 2022-10-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='expired_notification_sent',
            field=models.BooleanField(default=False, verbose_name='Expired notification sent'),
        ),
    ]
