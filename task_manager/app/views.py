from django.shortcuts import render

# Create your views here.
def list_tasks(request):
    title = 'List tasks'

    return render(request, 'tasks/list_tasks.html', {'title': title})
