from django.test import TestCase

from vendor_app.tests.vendor_factory import VendorFactory

from ..models import PurchaseOrder
from .order_factory import PurchaseOrderFactory


class PurchaseOrderTest(TestCase):
    def test_purchase_order_creation(self):
        # Creating a Vendor instance using the factory
        vendor = VendorFactory()

        # Use the PurchaseOrderFactory to create a PurchaseOrder instance
        purchase_order = PurchaseOrderFactory(vendor=vendor)

        # Retrieve the PurchaseOrder from the database
        saved_purchase_order = PurchaseOrder.objects.get(pk=purchase_order.pk)

        # check if the data was saved correctly
        self.assertEqual(saved_purchase_order.po_number, purchase_order.po_number)
        self.assertEqual(saved_purchase_order.vendor, vendor)
        self.assertEqual(saved_purchase_order.order_date, purchase_order.order_date)

        self.assertEqual(saved_purchase_order.items, purchase_order.items)
        self.assertEqual(saved_purchase_order.quantity, purchase_order.quantity)
        self.assertEqual(saved_purchase_order.status, purchase_order.status)
        self.assertEqual(
            saved_purchase_order.quality_rating, purchase_order.quality_rating
        )
