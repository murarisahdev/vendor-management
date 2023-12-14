from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PurchaseOrder


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    vendor = instance.vendor
    if instance.status == "completed":
        # On-Time Delivery Rate
        vendor.on_time_delivery_rate = instance.calculate_on_time_delivery_rate()

        # Quality Rating Average
        if instance.quality_rating is not None:
            vendor.quality_rating_avg = instance.calculate_quality_rating_avg()

    # Average Response Time
    if instance.acknowledgment_date is not None:
        vendor.average_response_time = instance.calculate_average_response_time()

    # Fulfilment Rate
    vendor.fulfillment_rate = instance.calculate_fulfillment_rate()

    # Save changes to the vendor model
    vendor.save()
