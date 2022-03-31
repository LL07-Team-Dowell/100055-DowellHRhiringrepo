from django.urls import path
from . import views

app_name='JobPortal_App'


urlpatterns = [
    path('', views.JobList.as_view(), name='job_list'),
    path('application/<int:pk>/',views.fill_application, name='application'),
    path('apply/<int:pk>/',views.apply_role, name='apply'),
    path('details/<int:pk>/',views.job_details, name='details'),
    
]