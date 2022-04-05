from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class MyCustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'bio', 'avatar', 'password')
