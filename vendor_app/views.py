from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import HistoricalPerformance, Vendor
from .serializers import (
    HistoricalPerformanceSerializer,
    VendorPerformanceSerializer,
    VendorSerializer,
)


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get_permissions(self):
        if self.action == "create" and self.request.method == "POST":
            # Set AllowAny permission for the 'create' action only for POST requests
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    @action(detail=True, methods=["get"])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        serializer = VendorPerformanceSerializer(vendor)
        return Response(serializer.data)


class HistoricalPerformanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
