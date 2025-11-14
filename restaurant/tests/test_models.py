from django.test import TestCase
from restaurant.models import Booking, Menu
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class MenuModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username="admin",
            password="littlelemon",
            email="admin@example.com"
        )
        self.client.force_authenticate(user=self.admin_user)

    def test_create_menu_item(self):
        item = Menu.objects.create(
            title="Burger",
            price=12.99,
            description="Juicy grilled burger"
        )
        self.assertEqual(item.title, "Burger")
        self.assertEqual(item.price, 12.99)

class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            customer_name="John Doe",
            customer_email="john.doe@example.com",  
            booking_date="2024-12-25 19:00",
            number_of_people=4
        )
        self.assertEqual(booking.customer_name, "John Doe")
        self.assertEqual(booking.number_of_people, 4)
