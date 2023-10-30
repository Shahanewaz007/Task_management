from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            
            task = Task.objects.create(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                due_date = form.cleaned_data['due_date'],
                priority = form.cleaned_data['priority'],
            )
            task.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form':form})


def task_list(request):
    
    task = Task.objects.all()
    print(task)
    return render(request, 'task_list.html', {'task' : task})