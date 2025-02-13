from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'updated', 'created')  # Ensure all these fields exist
    list_filter = ('status',)  # 'capacity' and 'location' do not exist in your Room model

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'guest_name', 'guest_email', 'start_date', 'end_date', 'created')  
    list_filter = ('start_date', 'end_date')  # These fields exist in Booking model
