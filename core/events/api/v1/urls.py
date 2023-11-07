from events.api.v1 import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("event", views.EventModelViewSet, basename="event")

urlpatterns = router.urls
