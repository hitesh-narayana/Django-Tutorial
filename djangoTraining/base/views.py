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
   return render(request, 'home.html', {'rooms':rooms})

def room(request):
    return render(request, 'room.html')
