from django import template
from base.models import Booking

register = template.Library()

@register.filter(name='get_item')
def get_item(value, key):
    """Return bookings for the specified room."""
    return Booking.objects.filter(room_id=key)

