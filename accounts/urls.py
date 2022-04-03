from django.urls import path, include
from accounts import views

urlpatterns = [
    path('api/login/', views.login, name="login"),
    path('api/logout/', views.logout, name="logout"),
    path('api/signup/', views.signup, name="signup"),
]
