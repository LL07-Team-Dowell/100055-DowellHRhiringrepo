from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, User


class MyCustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['__all__']
