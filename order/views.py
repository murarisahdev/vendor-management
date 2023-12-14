from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    @action(detail=True, methods=["post"])
    def acknowledge(self, request, pk=None):
        purchase_order = self.get_object()
        # check acknowledgment_date is already set
        if purchase_order.acknowledgment_date is not None:
            raise ValidationError({"error": "Purchase Order Already Acknowledged"})

        # Set the acknowledgment_date to the current time
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        # Calculate and update vendor performance metrics

        purchase_order.vendor.average_response_time = (
            purchase_order.calculate_average_response_time()
        )
        purchase_order.vendor.save()
        serializer = self.get_serializer(purchase_order)
        return Response(serializer.data, status=status.HTTP_200_OK)
