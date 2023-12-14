from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .test_login import UserAuthenticationTests
from .vendor_factory import HistoricalPerformanceFactory, UserFactory, VendorFactory


class VendorModalTestCase(UserAuthenticationTests):
    def setUp(self):
        super().setUp()
        self.test_successful_login_returns_access_token()
        self.access_token = self.access_token
        self.header = {"Authorization": f"Bearer {self.access_token}"}

        # Creating a vendor instance using the VendorFactory
        self.vendor = VendorFactory.create(user=self.user)
        self.url = reverse("vendor-list")

    def test_list_vendors_success(self):
        response = self.client.get(
            self.url,
            format="json",
            headers=self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class HistoricalPerformanceModalTestCase(UserAuthenticationTests):
    def setUp(self):
        super().setUp()
        self.test_successful_login_returns_access_token()
        self.access_token = self.access_token
        self.header = {"Authorization": f"Bearer {self.access_token}"}

        # Creating a vendor instance using the VendorFactory
        self.vendor = VendorFactory.create(user=self.user)

        self.historical_performance = HistoricalPerformanceFactory.create(
            vendor=self.vendor
        )
        self.url = reverse("historical-performance-list")

    def test_list_vendors_success(self):
        response = self.client.get(
            self.url,
            format="json",
            headers=self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
