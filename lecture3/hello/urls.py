from django.urls import path
from . import views


urlpatterns = [
    # url path, view to be parsed
    path("", views.index, name="index"),
    path("universe", views.universe, name="universe"),
    # here we tell django, that any string that goes after /hello/ can be matched
    # and saved in the name variable. then the greet methods should be invoked
    # with the name variable as argument
    path("<str:name>", views.greet, name="greet")
]
