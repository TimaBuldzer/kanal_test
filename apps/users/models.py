from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    tg_id = models.BigIntegerField(unique=True, verbose_name='Telegram ID')
    REQUIRED_FIELDS = ['tg_id']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-id']

    def __str__(self):
        return f'User {self.username}'
