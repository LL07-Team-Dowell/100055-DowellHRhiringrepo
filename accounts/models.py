from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# import jsonfield
# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    country = models.CharField(max_length=132, null=True)
    bio = models.TextField(null=True)
    # default="avatar.svg") to be uncommented after setting up a default image
    avatar = models.ImageField(null=True)
    JobTitle = models.CharField(max_length=132, null=True)
    position = models.CharField(max_length=132, null=True)
    is_hr = models.BooleanField(default=False, null=True)
    is_team_leader = models.BooleanField(default=False, null=True)

    def str(self):
        return f'{self.username}, {self.email}'


class Job(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    specific_t_n_c = models.TextField()
    status = models.CharField(
        max_length=100, default="Not Receiving Applications")

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    feedBack = models.TextField(null=True)
    freelancePlatform = models.CharField(max_length=132, null=True)
    freelancePlatformUrl = models.URLField(null=True)
    status = models.CharField(max_length=132, null=True, default="Pending")
    qualification = models.CharField(max_length=132, null=True)
    General_Terms_Conditions = models.JSONField()
    Technical_Specifications = models.JSONField()
    Payment_terms = models.JSONField()
    others = models.JSONField()

    def str(self):
        return f'{self.job}, {self.user}'
