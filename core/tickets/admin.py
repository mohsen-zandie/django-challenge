from django.contrib import admin

from tickets.models import Ticket, Basket

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


class BasketAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "ticket",
        "is_paid",
        "created_at",
        "updated_at",
    )
    list_filter = ("user", "ticket", "is_paid", "created_at", "updated_at")
    search_fields = (
        "user",
        "ticket",
        "is_paid",
        "created_at",
        "updated_at",
    )


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Basket, BasketAdmin)
