from curses.ascii import HT
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import CustomUser
from .serializers import CustomUserSerializer, CustomUserViewSet
from .forms import MyCustomUserCreationForm
# Create your views here.


@api_view(['POST'])
def login(request):
    page = 'login'
    if request.user.is_authenticated:
        messages.success(request, "User is already Logged in")
        return redirect('home')

    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, f'Welcome {user.username}, You have successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or Password')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


@api_view(['GET', 'POST'])
def signup(request, pk):
    page = "register"
    form = MyCustomUserCreationForm()
    context = {'page': page, 'form': form}
    if request.method == 'POST':
        form = MyCustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            HTTPResponse("You Have Successfully signed up for Dowell")
            login(request, user)
        else:
            HTTPResponse("Some error occured")
            #messages.error(request, 'An error occured')


@api_view(['GET'])
def logout(request):
    logout(request)
    HTTPResponse("You Have Successfully logged out")
