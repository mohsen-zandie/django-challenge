from django.urls import path
from django.urls.conf import include


app_name = "stadiums"

urlpatterns = [
    path("api/v1/", include("stadiums.api.v1.urls")),
]
