from django.contrib import admin
from events.models.events import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "stadium",
        "date",
        "description",
        "price",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
        "stadium",
        "date",
        "description",
        "price",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "stadium",
        "date",
        "description",
        "price",
        "created_at",
        "updated_at",
    )


admin.site.register(Event, EventAdmin)
