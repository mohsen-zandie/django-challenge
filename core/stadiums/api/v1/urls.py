from stadiums.api.v1 import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("stadium", views.StadiumModelViewSet, basename="stadium")
router.register("stadium-plan", views.StadiumPlanModelViewSet,
                basename="stadium-plan")

urlpatterns = router.urls
