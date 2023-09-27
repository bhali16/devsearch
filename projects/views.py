from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    context = {}
    return render(request, 'projects/projects.html', context)
