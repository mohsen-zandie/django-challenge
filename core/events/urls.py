from django.urls import path
from django.urls.conf import include


app_name = "events"

urlpatterns = [
    path("api/v1/", include("events.api.v1.urls")),
]
