from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): 
    # return HttpResponse("Hello world from hello project")
    return render(request, "hello/index.html")

def jeff(request): 
    return HttpResponse("Hi from jeff")

def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}")