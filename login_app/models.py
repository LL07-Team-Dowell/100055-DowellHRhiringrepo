from django.db import models
from django.db import IntegrityError, models, router, transaction
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.fields import BooleanField
from django.utils.translation import gettext_lazy

# Create your models here.





class MyUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email Must be Set")

        email=self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser Must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError ('Super must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)


class User (AbstractBaseUser, PermissionsMixin):
    email =models.EmailField(unique=True, null=False)
    form_submitted=models.BooleanField(default=False)
    is_staff = models.BooleanField (gettext_lazy('staff Status'), default=False, help_text =gettext_lazy('Designates whether the user can log in the site'))
    is_active=models.BooleanField(gettext_lazy('active'), default=True, help_text= gettext_lazy('Designates whether this user should be treated as active'))

    USERNAME_FIELD= 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
