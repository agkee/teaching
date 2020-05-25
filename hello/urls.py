from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jeff", views.jeff, name="Jeff"),
    # Accepts any string with its parameter in name 
    path("<str:name>", views.greet, name="greet"),
]