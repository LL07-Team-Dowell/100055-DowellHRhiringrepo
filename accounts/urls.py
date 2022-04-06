from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
from accounts import views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/hrview/', views.hrview, name="hrview"),
    path('api/candindateview/', views.candindateview, name="candindateview"),
    path('api/create_job/', views.create_job, name="create_job"),
    path('api/get_jobs/', views.get_jobs, name="get_jobs"),
    path('api/update_job/', views.update_job, name="update_job"),
    path('api/delete_job/', views.delete_job, name="delete_job"),
    path('api/get_applications/', views.get_applications, name="get_applications"),
    path('api/get_jobs/', views.get_jobs, name="get_jobs"),
]
