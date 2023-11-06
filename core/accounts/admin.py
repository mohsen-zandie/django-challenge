from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
from accounts.models import Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        ('Authentication', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        ('Authentication', {'fields': ('email', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
