from django.shortcuts import render
from django.http import HttpResponse

from .models import Room, Booking
from .forms import BookingForm

# Create your views here.

# rooms=[
#     {'id':1, 'name':'Room 1', 'status':'Open'},
#     {'id':2, 'name':'Room 2', 'status':'Open'},
#     {'id':3, 'name':'Room 3', 'status':'Closed'},
#     {'id':4, 'name':'Room 4', 'status':'Open'},
#     {'id':5, 'name':'Room 5', 'status':'Closed'},
# ]


def home(request):
    rooms = Room.objects.all()
    bookings = Booking.objects.all()
    room_bookings = {}

    for room in rooms:
        room_bookings[room.id] = bookings.filter(room=room)

    context = {'rooms': rooms, 'room_bookings': room_bookings}
    return render(request, 'home.html', context)


def room(request,pk):
    rooms = Room.objects.get(id=pk)
    context = {'room':rooms}
    return render(request, 'room.html',context)


def bookings(request):
   form = BookingForm()
   context ={'form':form}
   return render(request,'booking_form.html',context)