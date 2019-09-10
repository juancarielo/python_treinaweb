from django.shortcuts import render

def list(request):
    title = 'List'
    return render(request, 'task/list.html', {'title': title})