from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request): 
    # return HttpResponse("Hello world from hello project")
    return render(request, "hello/index.html")

def greet(request, name):
    # return HttpResponse(f"Hello {name.capitalize()}")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })

def calculator(request, first, second):
    return HttpResponse(first + second)

def currentDate(request): 
    curr = datetime.now() 
    print(curr)
    return render(request, "hello/time.html", {
        "monday": datetime.today().strftime("%A") == "Monday",
        "tuesday": datetime.today().strftime("%A") == "Tuesday",
        "wednesday": datetime.today().strftime("%A") == "Wednesday",
        "thursday": datetime.today().strftime("%A") == "Thursday",
        "friday": datetime.today().strftime("%A") == "Friday",
        "saturday": datetime.today().strftime("%A") == "Saturday",
        "sunday": datetime.today().strftime("%A") == "Sunday"
    })