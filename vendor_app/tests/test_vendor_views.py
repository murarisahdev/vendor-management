from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .test_login import UserAuthenticationTests
from .vendor_factory import HistoricalPerformanceFactory, UserFactory, VendorFactory


class VendorViewSetTestCase(UserAuthenticationTests):
    def setUp(self):
        super().setUp()
        self.test_successful_login_returns_access_token()
        self.access_token = self.access_token
        self.header = {"Authorization": f"Bearer {self.access_token}"}

        # Creating a vendor instance using the VendorFactory
        self.vendor = VendorFactory.create(user=self.user)
        self.url = reverse("vendor-list")

    def test_create_vendor_success(self):
        data = {
            "name": "New Vendor",
            "user": UserFactory().id,
            "contact_details": "New Vendor Contact Details",
            "address": "New Vendor Address",
            "vendor_code": "67890",
        }
        response = self.client.post(
            self.url,
            data,
            format="json",
            headers=self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_vendor_with_existing_user(self):
        data = {
            "name": "New Vendor",
            "user": self.user.id,
            "contact_details": "New Vendor Contact Details",
            "address": "New Vendor Address",
            "vendor_code": "67890",
        }
        response = self.client.post(
            self.url,
            data,
            format="json",
            headers=self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_vendor_success(self):
        updated_data = {"name": "Updated Vendor Name"}
        response = self.client.patch(
            reverse("vendor-detail", kwargs={"pk": self.vendor.id}),
            updated_data,
            format="json",
            headers=self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendor.refresh_from_db()
        self.assertEqual(self.vendor.name, "Updated Vendor Name")

    def test_list_vendors_success(self):
        vendor1 = VendorFactory()
        vendor2 = VendorFactory()
        response = self.client.get(
            self.url,
            format="json",
            headers=self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_delete_vendor_success(self):
        vendor = VendorFactory()
        url = reverse("vendor-detail", kwargs={"pk": self.vendor.id})
        response = self.client.delete(
            url,
            format="json",
            headers=self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_vendor_with_invalid_id(self):
        vendor = VendorFactory()
        url = reverse("vendor-detail", kwargs={"pk": -20})
        response = self.client.delete(
            url,
            format="json",
            headers=self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_vendor_not_found(self):
        url = reverse("vendor-detail", kwargs={"pk": -20})
        response = self.client.get(
            url,
            format="json",
            headers=self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_vendor_performance_success(self):
        vendor = VendorFactory()
        url = f'{reverse("vendor-detail", kwargs={"pk":vendor.id})}performance/'
        response = self.client.get(
            url,
            format="json",
            headers=self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
