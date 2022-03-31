
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from login_app.form import SignUpForm


def sign_up(request):
    form=SignUpForm()
    registered=False
    if request.method=='POST':
        form=SignUpForm(data=request.POST)
        if  form.is_valid():
            form.save()
            registered=True
    dict={'form':form, 'registered':registered}
    return render(request, 'login_app/sign_up.html', context=dict)

def login_page(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('JobPortal_App:job_list'))
    return render (request, 'login_app/login.html', context={'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:login'))

