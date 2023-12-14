from datetime import datetime, timedelta

import factory
from factory.django import DjangoModelFactory

from vendor_app.tests.vendor_factory import VendorFactory

from ..models import PurchaseOrder


class PurchaseOrderFactory(DjangoModelFactory):
    class Meta:
        model = PurchaseOrder

    po_number = factory.Sequence(lambda n: f"PO{n:05d}")
    vendor = factory.SubFactory(VendorFactory)
    order_date = factory.Faker("date_time_this_decade", tzinfo=None)
    delivery_date = factory.Faker("date_time_this_decade", tzinfo=None)
    items = factory.Faker("pydict", nb_elements=2)
    quantity = factory.Faker("random_int", min=1, max=100)
    status = PurchaseOrder.PurchaseOrderStatus.PENDING
    quality_rating = factory.Faker("pyfloat", positive=True)
    issue_date = factory.Faker("date_time_this_decade", tzinfo=None)
    acknowledgment_date = factory.Faker("date_time_this_decade", tzinfo=None)
