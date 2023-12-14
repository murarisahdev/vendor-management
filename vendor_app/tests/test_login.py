# tests.py
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .vendor_factory import UserFactory


class UserAuthenticationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Defining the URL for user login
        self.login_url = reverse("user-signin")

        # Creating a user instance using the UserFactory
        self.user = UserFactory()

        # Updating the user password using make_password
        self.user.password = make_password("mypassword")
        self.user.save()

        # Set up user_data for login
        self.valid_credentials = {
            "username": self.user.username,
            "password": "mypassword",
        }

    # Testing successful login returns an access token
    def test_successful_login_returns_access_token(self):
        response = self.client.post(
            self.login_url, self.valid_credentials, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.access_token = response.data["access"]
