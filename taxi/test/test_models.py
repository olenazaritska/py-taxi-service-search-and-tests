from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(
            name="test_manufacturer",
            country="test_country"
        )
        self.assertEqual(
            str(manufacturer),
            f"{manufacturer.name} {manufacturer.country}"
        )

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="test_driver",
            password="test_password",
            first_name="test_first_name",
            last_name="test_last_name",
        )
        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(
            name="test_manufacturer",
            country="test_country"
        )
        driver = get_user_model().objects.create(
            username="test_driver",
            password="test_password",
            first_name="test_first_name",
            last_name="test_last_name",
        )
        car = Car.objects.create(model="test_model", manufacturer=manufacturer)
        car.drivers.set((driver,))
        self.assertEqual(str(car), car.model)

    def test_create_driver_with_license(self):
        username = "test_driver"
        password = "test_password"
        license_number = "test_license_number"

        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number,
        )
        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)

    def test_deriver_get_absolute_url(self):
        driver = get_user_model().objects.create_user(
            username="test_driver",
            password="test_password",
        )
        self.assertEqual(driver.get_absolute_url(), "/drivers/1/")