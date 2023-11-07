from django.contrib import admin

from tickets.models import Ticket

# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "event",
        "user",
        "seat",
        "price",
        "created_at",
        "updated_at",
    )
    list_filter = ("event", "user", "created_at", "updated_at")
    search_fields = (
        "event",
        "user",
        "seat",
        "price",
        "created_at",
        "updated_at",
    )


admin.site.register(Ticket, TicketAdmin)
