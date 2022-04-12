from django.contrib import admin

# Register your models here.
from .models import JobApplication,NewJobsApplication,HRCanidateStatus , TMCanidateStatus , AccountsCanidateStatus, InternetSpeed

admin.site.register(JobApplication)
admin.site.register(NewJobsApplication)
admin.site.register(HRCanidateStatus)
admin.site.register(AccountsCanidateStatus)
admin.site.register(TMCanidateStatus)
admin.site.register(InternetSpeed)
