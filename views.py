from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

def index (request):
    return HttpResponseRedirect(reverse('JobPortal_App:job_list'))
