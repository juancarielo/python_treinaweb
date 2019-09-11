from django.shortcuts import render, redirect
from .forms import TaskForm
from .entities.task import Task
from .services import task_service


def list(request):
    title = 'List'
    tasks = task_service.list()
    return render(request, 'task/list.html', {'title': title, 'tasks': tasks})

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            date_expiration = form.cleaned_data['date_expiration']
            priority = form.cleaned_data['priority']

            new_task = Task(
                title = title,
                description = description,
                date_expiration = date_expiration,
                priority = priority
            )

            # insert new task
            task_service.create(new_task)

            return redirect('list')
    else:
        form = TaskForm()

    title = 'Create'
    return render(request, 'task/form.html', {'title': title, 'form': form})

def edit(request, id):
    edit_task = task_service.find_by_id(id)
    form = TaskForm(request.POST or None, instance=edit_task)
    
    if form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        date_expiration = form.cleaned_data['date_expiration']
        priority = form.cleaned_data['priority']

        new_task = Task(
            title = title,
            description = description,
            date_expiration = date_expiration,
            priority = priority
        )

        task_service.edit(edit_task, new_task)
        
        return redirect('list')
    
    title = 'Edit'
    return render(request, 'task/form.html', {'title': title, 'form': form})

def delete(request, id):
    task = task_service.find_by_id(id)

    if request.method == 'POST':
        task_service.delete(task)

        return redirect('list')
    
    title = 'Delete'
    return render(request, 'task/delete.html', {'title': title, 'task': task})
