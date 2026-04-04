from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectTypes
# Create your views here.

def all_projects(request):
    projects = ProjectTypes.objects.all()
    return render(request,'project/index.html', {'projects':projects})