from django.test import TestCase
from .models import Room, Booking
from datetime import date
# Create your tests here.

class BookingModelTest(TestCase):

    def setUp(self):
        self.room = Room.objects.create(
            name='Test Room',
            description='A room for testing',
            status='Open'
        )
        self.booking = Booking.objects.create(
            room=self.room,
            start_date=date(2023, 1, 1),
            end_date=date(2023, 1, 2),
            guest_name='John Doe',
            guest_email='john.doe@example.com',
            guest_phone='1234567890'
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.guest_name, 'John Doe')
        self.assertEqual(self.booking.guest_email, 'john.doe@example.com')
        self.assertEqual(self.booking.guest_phone, '1234567890')
        self.assertEqual(self.booking.room, self.room)
        self.assertEqual(self.booking.start_date, date(2023, 1, 1))
        self.assertEqual(self.booking.end_date, date(2023, 1, 2))

    def test_booking_str(self):
        self.assertEqual(str(self.booking), 'John Doe')