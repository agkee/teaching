from django.urls import path
from . import views

urlpatterns = [
    # path(url, which handler, name to reference from other parts of the app)
    path("", views.index, name="index"),
    path("jeff", views.jeff, name="Jeff"),
    # Accepts any string with its parameter in name 
    path("<str:name>", views.greet, name="greet"),
]