from rest_framework.routers import DefaultRouter

from apps.eightpercent.views import DepositViewSet

app_name = "eightpercent"

router = DefaultRouter()
router.register(r"deposits", DepositViewSet)


urlpatterns = router.urls
