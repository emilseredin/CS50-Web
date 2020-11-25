import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    # one way of doing this
    # answer = "NO"
    # if now.month == 1 and now.day == 1:
    #     answer = "YES"
    # return render(request, "new_year/index.html", {
    #     "answer": answer
    # })
    # another way us to send True or False to the template
    # and then implement the logic there
    return render(request, "new_year/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })