from django.shortcuts import render, HttpResponse

# Create your views here.


def login(request):
    return HttpResponse("This is login page")
    pass


def logout(request):
    return HttpResponse("This is logout page")
    pass


def signup(request):
    return HttpResponse("This is signup page")
    pass
