import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from ..models import HistoricalPerformance, Vendor


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = "mypassword"


class VendorFactory(DjangoModelFactory):
    class Meta:
        model = Vendor

    user = factory.SubFactory(UserFactory)
    name = factory.Faker("company")
    contact_details = factory.Faker("paragraph")
    address = factory.Faker("address")
    vendor_code = factory.Sequence(lambda n: f"vendor_{n}")
    on_time_delivery_rate = factory.Faker("pyfloat", left_digits=2, right_digits=2)
    quality_rating_avg = factory.Faker("pyfloat", left_digits=2, right_digits=2)
    average_response_time = factory.Faker("pyfloat", left_digits=2, right_digits=2)
    fulfillment_rate = factory.Faker("pyfloat", left_digits=2, right_digits=2)


class HistoricalPerformanceFactory(DjangoModelFactory):
    class Meta:
        model = HistoricalPerformance

    vendor = factory.SubFactory(VendorFactory)
    on_time_delivery_rate = factory.Faker("pyfloat", left_digits=2, right_digits=2)
    quality_rating_avg = factory.Faker("pyfloat", left_digits=2, right_digits=2)
    average_response_time = factory.Faker("pyfloat", left_digits=2, right_digits=2)
    fulfillment_rate = factory.Faker("pyfloat", left_digits=2, right_digits=2)
