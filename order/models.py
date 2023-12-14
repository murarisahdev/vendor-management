from django.db import models
from django.db.models import Avg

from vendor_app.models import Vendor


class PurchaseOrder(models.Model):
    # Defining choices for purchase order using the TextChoices enumeration
    class PurchaseOrderStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETED = "completed", "Completed"
        CANCELED = "canceled", "Canceled"

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="purchase_orders"
    )

    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=PurchaseOrderStatus.choices,
        default=PurchaseOrderStatus.PENDING,
    )
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.po_number:
            # Generate a readable unique po_number
            last_purchase_order = PurchaseOrder.objects.order_by("-id").first()
            new_id = (last_purchase_order.id + 1) if last_purchase_order else 1
            self.po_number = f"PO{new_id}"

        super().save(*args, **kwargs)

    def calculate_on_time_delivery_rate(self):
        completed_pos = self.vendor.purchase_orders.filter(status="completed")
        on_time_deliveries = completed_pos.filter(
            delivery_date__lte=models.F("acknowledgment_date")
        )
        return (
            (on_time_deliveries.count() / completed_pos.count()) * 100
            if completed_pos.count()
            else 0
        )

    def calculate_quality_rating_avg(self):
        completed_pos = self.vendor.purchase_orders.filter(
            status="completed", quality_rating__isnull=False
        )
        return (
            completed_pos.aggregate(Avg("quality_rating"))["quality_rating__avg"] or 0.0
        )

    def calculate_average_response_time(self):
        acknowledged_pos = self.vendor.purchase_orders.filter(
            acknowledgment_date__isnull=False
        )
        response_times = [
            (po.acknowledgment_date - po.issue_date).total_seconds()
            for po in acknowledged_pos
        ]
        return sum(response_times) / len(response_times) if len(response_times) else 0.0

    def calculate_fulfillment_rate(self):
        all_pos = self.vendor.purchase_orders.all()
        fulfilled_pos = all_pos.filter(status="completed", issue_date__isnull=False)
        return (fulfilled_pos.count() / all_pos.count()) * 100 if all_pos.count() else 0
