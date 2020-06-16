from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

schools = ["school1", "school2", "school3"]

class NewSchoolForm(forms.Form): 
    school = forms.CharField(label="New School")
    size = forms.IntegerField(label="Student body size", min_value=1000, max_value=1000000)

# Create your views here.
def index(request): 
    # if "schools" not in request.session: 
    #     request.session["schools"] = []

    return render(request, "schools/index.html", {
        "schools": schools,
        # "schools": request.session["schools"]
    })


# Will throw error and should run python manage.py migrate because we have to initialize table
# For request.session
    # return render(request, "schools/index.html", {
    #     "schools": request.session["schools"]
    # })

def addSchool(request): 
    return render(request, "schools/addSchool.html")

def addSchoolLibrary(request): 
    # When the incoming request is POST method
    if request.method == "POST": 
        form = NewSchoolForm(request.POST) 
        if form.is_valid(): 
            school = form.cleaned_data["school"] 
            schools.append(school)
            # request.session["schools"] += [school]
            return HttpResponseRedirect(reverse("schools:index"))
        else: 
            return render(request, "schools/addSchool.html", {
                "form": form
            })

    # When the incoming request is GET method
    return render(request, "schools/addSchoolLibrary.html", {
        "form": NewSchoolForm()
    })