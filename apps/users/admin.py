from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'tg_id', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
    list_display_links = ('id', 'username')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_per_page = 25
