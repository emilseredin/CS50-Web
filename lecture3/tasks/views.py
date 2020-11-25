from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTaskForm(forms.Form):
    # provide all form fields
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(
        label="Priority",
        min_value=1,
        max_value=5
    )

# Create your views here.
def index(request):
    # check if it is a new request or the recurring one
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(
        request, 
        "tasks/index.html",
        { "tasks": request.session["tasks"] }
    )

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # append the new task to the session
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(
                request,
                "tasks/add.html",
                # send back the form that has just been received 
                # so that the errors are sent to the user as well
                { "form": form }
            )

    return render(
        request,
        "tasks/add.html", 
        { "form": NewTaskForm }
)
