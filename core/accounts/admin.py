from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
