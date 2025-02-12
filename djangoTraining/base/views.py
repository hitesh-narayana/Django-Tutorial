from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms=[
    {'id':1, 'name':'Room 1', 'status':'Open'},
    {'id':2, 'name':'Room 2', 'status':'Open'},
    {'id':3, 'name':'Room 3', 'status':'Closed'},
    {'id':4, 'name':'Room 4', 'status':'Open'},
    {'id':5, 'name':'Room 5', 'status':'Closed'},
]

def home(request):
   context = {'rooms':rooms}
   return render(request, 'home.html', context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i;
    context = {'room':room}
    return render(request, 'room.html',context)
