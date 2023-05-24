from django.shortcuts import render, redirect
from .models import Desk
from .forms import DeskForm


def home(request):
    desks = Desk.objects.all()
    context = {'desks':desks}
    return render(request, 'base/home.html', context)

def desk(request, pk):
    desk = Desk.objects.get(id=pk)
    context = {'desk':desk}
    return render(request, 'base/desk.html', context)

def createDesk(request):
    form = DeskForm()
    if request.method == 'POST':
        form = DeskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/desk_form.html', context)

def updateDesk(request, pk):
    desk = Desk.objects.get(id=pk)
    form = DeskForm(instance=desk)

    if request.method == 'POST':
        form = DeskForm(request.POST, instance=desk)
        if form.is_valid():
            print("Done")
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/desk_form.html', context)

def deleteDesk(request, pk):
    desk = Desk.objects.get(id=pk)
    if request.method == 'POST':
        desk.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':desk})