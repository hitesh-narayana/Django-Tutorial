from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Room,Booking
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
    room_bookings = {room.id: room.booking_set.all() for room in rooms}
    context = {'rooms': rooms, 'room_bookings': room_bookings}
    return render(request, 'home.html', context)


def room(request,pk):
    rooms = Room.objects.get(id=pk)
    context = {'room':rooms}
    return render(request, 'room.html',context)


def bookings(request):
   form = BookingForm()
   if request.method == 'POST':
       print(request.POST)
       form = BookingForm(request.POST)
       if form.is_valid():
           booking = form.save()

           room = booking.room
           room.status = 'Closed'
           room.save()
           return redirect('home')
   context ={'form':form}
   return render(request,'booking_form.html',context)