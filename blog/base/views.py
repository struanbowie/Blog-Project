from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Desk, Topic
from .forms import DeskForm


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    desks = Desk.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(name__icontains=q) | 
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()

    desk_count = desks.count()

    context = {'desks':desks, 'topics':topics, 'desk_count':desk_count}
    return render(request, 'base/home.html', context)

def desk(request, pk):
    desk = Desk.objects.get(id=pk)
    desk_post = desk.post_set.all()
    context = {'desk':desk, 'desk_post':desk_post}
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

# def post(request, pk):
#     post = Post.objects.get(id=pk)
#     context = {'post':post}
#     return render(request, 'base/desk.html', context)

# def createPost(request):
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')

#     context = {'form':form}
#     return render(request, 'base/desk.html', context)