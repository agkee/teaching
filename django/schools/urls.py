from django.urls import path
from . import views

app_name = "schools"

urlpatterns = [
    path("", views.index, name="index"),
    path("addSchool", views.addSchool, name="addSchool"),
    path("addSchoolLibrary", views.addSchoolLibrary, name="addSchoolLibrary"),
]