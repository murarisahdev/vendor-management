from django.contrib.auth.models import User
from rest_framework import serializers

from .models import HistoricalPerformance, Vendor


class VendorSerializer(serializers.ModelSerializer):  # TODO
    class Meta:
        model = Vendor
        fields = "__all__"


class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]


class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = "__all__"
