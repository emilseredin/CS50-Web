from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # use a separate folder for the app to namespace all html files, so that files 
    # with the same names, but used by different apps don't conflict with each other
    return render(request, "hello/index.html")


def universe(request):
    return HttpResponse("Hello Universe!")


# def greet(request, name):
#     return HttpResponse("Hello, {}!".format(name.capitalize()))
def greet(request, name):
    # additional context is provided by the third dictionary argument
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })