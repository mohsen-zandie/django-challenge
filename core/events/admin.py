from django.contrib import admin
from events.models import Stadium, Event


class StadiumAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'city', 'country',
                    'address', 'opened', 'created_at', 'updated_at')
    list_filter = ('name', 'capacity', 'city', 'country',
                   'address', 'opened', 'created_at', 'updated_at')
    search_fields = ('name', 'capacity', 'city', 'country',
                     'address', 'opened', 'created_at', 'updated_at')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'stadium', 'date', 'description',
                    'price', 'created_at', 'updated_at')
    list_filter = ('name', 'stadium', 'date', 'description',
                   'price', 'created_at', 'updated_at')
    search_fields = ('name', 'stadium', 'date', 'description',
                     'price', 'created_at', 'updated_at')


admin.site.register(Stadium, StadiumAdmin)
admin.site.register(Event, EventAdmin)
