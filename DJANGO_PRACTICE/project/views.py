from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def all_projects(request):
    return render(request,'project/index.html')