from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField
from django.conf import settings


# Create your models here.

class CreateJobs (models.Model):
    job_title=models.CharField(max_length=100, null=False, verbose_name='Discriptive Name')
    card_image=models.ImageField(upload_to='job_images', null=False, height_field=None, width_field=None, verbose_name="Descriptive Image For The Job")
    technical_specification=models.TextField(max_length=1000, null=False, unique=False, blank=False, verbose_name=_("Job Technical Specification"), help_text=_("format: required, max-1000"),)
    terms_and_conditions=models.TextField(max_length=1000, null=False, unique=False, blank=False, verbose_name=_("Job Terms and Conditons"), help_text=_("format: required, max-1000"),)
    payment_terms=models.TextField(max_length=1000, null=False, unique=False, blank=False, verbose_name=_("Job Payment Terms "), help_text=_("format: required, max-1000"),)



    def __str__(self):
        return self.job_title


class JobApplication (models.Model):
    FREELANCE_CHOICES=(
        ('up', 'Upwork'),
        ('FR', 'Fiver'),
        ('ES', 'Envato Studio'),
        ('PP', 'PeoplePerHour'),
        ('TO', 'Toptal'),
        ('MH', 'MarketerHire'),
        ('GU', 'Guru'),
        ('DC', 'DesignCrowd'),
        ('NX', 'Nexxt'),
        ('OS', 'OnSite'),
        ('CS', 'Crewscale'),
    )

    candidate=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='applicant',   on_delete=models.CASCADE, null=True)
    job=models.ForeignKey(CreateJobs, on_delete=models.CASCADE,  related_name='apply_job')
    country = CountryField(null=False, unique=False, blank=False)
    qualification=models.CharField(max_length=50,null=False, unique=False,  blank=False)
    freelancer_platform=models.CharField(max_length=100, null=False, unique=False, blank=False, choices=FREELANCE_CHOICES)
    freelancer_link = models.URLField(max_length = 200, null=False, unique=False, blank=False)
    discord_profile_id= models.URLField(max_length = 200, null=False, unique=False, blank=False)
    i_agree_to_terms_and_conditions=models.BooleanField( null=False, unique=False, blank=False,)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['-created']

    def __str__(self):
        return str(self.candidate)

class Apply(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, related_name='application_form')
    apply_job=models.ForeignKey(CreateJobs, related_name='jobs_applied', on_delete=models.CASCADE, unique=True)
