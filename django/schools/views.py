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
    return render(request, "schools/index.html", {
        "schools": schools
    })
    # if "schools" not in request.session: 
    #     request.session["schools"] = []

    # return render(request, "schools/index.html", {
    #     "schools": request.session["schools"]
    # })

def addSchool(request): 
    return render(request, "schools/addSchool.html")

def addSchoolLibrary(request): 
    if request.method == "POST": 
        form = NewSchoolForm(request.POST) 
        if form.is_valid(): 
            school = form.cleaned_data["school"] 
            schools.append(school)
            # with session
            request.session["schools"] += [school]
            return HttpResponseRedirect(reverse("schools:index"))
        else: 
            return render(request, "schools/addSchool.html", {
                "form": form
            })

    return render(request, "schools/addSchoolLibrary.html", {
        "form": NewSchoolForm()
    })