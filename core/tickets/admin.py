from django.contrib import admin

from tickets.models.tickets import Ticket
from tickets.models.baskets import Basket

# Register your models here.


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 0


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "event",
        "user",
        "basket",
        "seat",
        "price",
        "created_at",
        "updated_at",
    )
    list_filter = ("event", "user", "basket", "created_at", "updated_at")
    search_fields = (
        "event",
        "user",
        "basket",
        "seat",
        "price",
        "created_at",
        "updated_at",
    )


class BasketAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "is_paid",
        "created_at",
        "updated_at",
    )
    list_filter = ("user", "is_paid", "created_at", "updated_at")
    search_fields = (
        "user",
        "is_paid",
        "created_at",
        "updated_at",
    )
    inlines = [TicketInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)

    def tickets(self, obj):
        return "\n".join([ticket.__str__() for ticket in obj.ticket_set.all()])

    tickets.short_description = 'Tickets'


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Basket, BasketAdmin)
