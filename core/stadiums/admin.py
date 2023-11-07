from django.contrib import admin

from stadiums.models import Stadium, StadiumPlan


class StadiumAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
        "country",
        "address",
        "opened",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
        "city",
        "country",
        "address",
        "opened",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "city",
        "country",
        "address",
        "opened",
        "created_at",
        "updated_at",
    )


class StadiumPlanAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "stadium",
        "rows",
        "columns",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
        "stadium",
        "rows",
        "columns",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "stadium",
        "rows",
        "columns",
        "created_at",
        "updated_at",
    )


admin.site.register(Stadium, StadiumAdmin)
admin.site.register(StadiumPlan, StadiumPlanAdmin)
