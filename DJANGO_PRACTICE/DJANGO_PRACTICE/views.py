from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("This is a home page1")

def contact(request):
    # return HttpResponse("This is a contact page")
    return render(request, "index.html") 