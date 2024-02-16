from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse 
from django import forms

class Task_form(forms.Form):
    task = forms.CharField(label = 'New task', max_length = 20)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "todo/index.html", {
        "tasks": request.session["tasks"]
    })

def add_task(request):
    if request.method == 'POST':
        form = Task_form(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, "todo/add_task.html", {
                "form": form
            })

    return render(request, "todo/add_task.html", {
        "form": Task_form()
    })