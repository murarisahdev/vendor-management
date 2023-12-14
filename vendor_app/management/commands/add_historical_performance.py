from django.core.management.base import BaseCommand
from django.utils import timezone

from vendor_app.models import HistoricalPerformance, Vendor


class Command(BaseCommand):
    help = "Update Historical Performance data for vendors"

    def handle(self, *args, **options):
        # fetch all vendors
        vendors = Vendor.objects.all()

        # Get the current timestamp
        current_time = timezone.now()

        # Create a list to hold all Historical Performance data
        historical_performance_list = []

        # Iterate through each vendor
        for vendor in vendors:
            # Create historical data record
            historical_data = HistoricalPerformance(
                vendor=vendor,
                date=current_time,
                on_time_delivery_rate=vendor.on_time_delivery_rate,
                quality_rating_avg=vendor.quality_rating_avg,
                average_response_time=vendor.average_response_time,
                fulfillment_rate=vendor.fulfillment_rate,
            )
            historical_performance_list.append(historical_data)

        # Bulk create all historical data records
        HistoricalPerformance.objects.bulk_create(historical_performance_list)

        self.stdout.write(
            self.style.SUCCESS("Successfully updated historical records for vendors")
        )
