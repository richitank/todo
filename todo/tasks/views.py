from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *


# Create your views here.

def index(request):   
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    tasks = Task.objects.all()
    # empty dictionary to pass the tasks in
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) # throws in new data when you use request.POST even through we are passing same instance that we fetched
        if form.is_valid():
            form.save()
            return redirect('/')

    context1 = {'form': form}

    return render(request, 'tasks/update_task.html', context1)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
        
    context = {'item': item}
    return render(request, 'tasks/delete.html', context)


