from django.urls import path
from . import views

app_name='login_app'


urlpatterns = [
    path('SignUp/', views.sign_up, name='SignUp'),
    path('login/', views.login_page, name='login'),
    path('sign_out/', views.logout_user, name='sign_out'),
   
]