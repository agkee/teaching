from django.urls import path
from . import views

urlpatterns = [
    # path(url, which handler, name to reference from other parts of the app)
    # localhost:8000/hello
    path("", views.index, name="index"),
    path("time", views.currentDate, name="time"),
    # Accepts any string with its parameter in name 
    path("<str:name>", views.greet, name="greet"),
    # path("calculator/<int:first>/<int:second>", views.calculator, name="calculator"),
]