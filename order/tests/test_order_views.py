from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from vendor_app.tests import test_login, vendor_factory

from ..models import PurchaseOrder
from .order_factory import PurchaseOrderFactory
from ..serializers import PurchaseOrderSerializer


class PurchaseOrderViewSetTest(test_login.UserAuthenticationTests):
    def setUp(self):
        super().setUp()
        self.vendor = vendor_factory.VendorFactory()
        self.url = reverse("purchase-order-list")

        self.test_successful_login_returns_access_token()
        self.access_token = self.access_token
        self.header = {"Authorization": f"Bearer {self.access_token}"}

    def test_create_purchase_order_success(self):
        data = {
            "po_number": "PO1",
            "vendor": self.vendor.id,
            "delivery_date": "2023-01-01T12:00:00Z",
            "items": {"item1": 5, "item2": 10},
            "quantity": str(Decimal("15")),
            "status": PurchaseOrder.PurchaseOrderStatus.PENDING,
            "issue_date": "2023-01-01T10:00:00Z",
        }

        response = self.client.post(
            self.url,
            data,
            format="json",
            headers=self.header,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 1)

    def test_create_purchase_order_with_empty_vendor(self):
        data = {
            "po_number": "PO1",
            "vendor": "",
            "delivery_date": "2023-01-01T12:00:00Z",
            "items": {"item1": 5, "item2": 10},
            "quantity": str(Decimal("15")),
            "status": PurchaseOrder.PurchaseOrderStatus.PENDING,
            "issue_date": "2023-01-01T10:00:00Z",
        }

        response = self.client.post(
            self.url,
            data,
            format="json",
            headers=self.header,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_purchase_order(self):
        purchase_order = PurchaseOrderFactory()
        url = reverse("purchase-order-detail", kwargs={"pk": purchase_order.pk})
        response = self.client.get(
            url,
            format="json",
            headers=self.header,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["po_number"], purchase_order.po_number)

    def test_update_purchase_order(self):
        purchase_order = PurchaseOrderFactory()
        data = {"status": "completed"}

        url = reverse("purchase-order-detail", kwargs={"pk": purchase_order.pk})
        response = self.client.patch(
            url,
            data,
            format="json",
            headers=self.header,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "completed")

    def test_delete_purchase_order(self):
        purchase_order = PurchaseOrderFactory()
        url = reverse("purchase-order-detail", kwargs={"pk": purchase_order.pk})
        response = self.client.delete(
            url,
            format="json",
            headers=self.header,
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PurchaseOrder.objects.count(), 0)
