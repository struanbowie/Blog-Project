from django.shortcuts import render
from .models import Desk


def home(request):
    desks = Desk.objects.all()
    context = {'desks':desks}
    return render(request, 'base/home.html', context)

def desk(request, pk):
    desk = Desk.objects.get(id=pk)
    context = {'desk':desk}
    return render(request, 'base/desk.html', context)
