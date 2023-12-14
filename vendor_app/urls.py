from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import HistoricalPerformanceViewSet, VendorViewSet

router = DefaultRouter()
router.register(r"vendors", VendorViewSet, basename="vendor")
router.register(
    r"historical-performance",
    HistoricalPerformanceViewSet,
    basename="historical-performance",
)

urlpatterns = [
    path("", include(router.urls)),
]
