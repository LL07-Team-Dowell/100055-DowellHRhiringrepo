from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from jobportal_app.forms import ApplicationForm

from jobportal_app.models import CreateJobs, JobApplication, Apply
from django.contrib import messages


# Create your views here.


class JobList(ListView):
    context_object_name = 'jobs'
    model = CreateJobs
    template_name = 'jobportal_app/job_list.html'


def job_details(request, pk):
    jobs=CreateJobs.objects.get(pk=pk)
    already_apply=Apply.objects.filter(apply_job=jobs, user=request.user)
    if already_apply:
        apply=True
    else:
        apply =False
    return render (request, 'jobportal_app/job_details.html', context= {'jobs':jobs,  'apply':apply})





@login_required
def apply_role(request, pk):
    jobs=CreateJobs.objects.get(pk=pk)
    user=request.user
    already_apply=Apply.objects.filter(jobs=jobs, user=user)
    if not already_apply:
        applied_job=Apply(jobs=jobs, user=user)
        applied_job.save()
    return HttpResponseRedirect(reverse('jobportal_app:fill_application', kwargs={'pk':pk}))


@login_required
def fill_application(request, pk):
    form=ApplicationForm(request.POST)
    if request.method=='POST' and request.user.is_authenticated:
        job=CreateJobs.objects.get(pk=pk)
        candidate=request.user
        user=candidate
        if not user.form_submitted and form.is_valid():
            form.save(commit=False)
            form.job=job
            form.candidate=candidate
            user.form_submitted=True
            form.save()
            messages.success(request, "Job Applied")
            return HttpResponseRedirect(reverse('JobPortal_App:job_list'))
        else:
            messages.warning(request, "Already Applied")
            return HttpResponseRedirect(reverse('JobPortal_App:job_list'))
    dict={'form':form }
    return render(request, 'jobportal_app/application.html', context=dict)
