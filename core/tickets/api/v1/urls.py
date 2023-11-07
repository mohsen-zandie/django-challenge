from tickets.api.v1 import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("ticket", views.TicketModelViewSet, basename="ticket")
router.register("basket", views.BasketModelViewSet, basename="basket")

urlpatterns = router.urls
