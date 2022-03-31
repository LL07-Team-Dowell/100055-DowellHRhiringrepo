from django import forms
from jobportal_app.models import JobApplication


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('country','qualification', 'freelancer_platform', 'freelancer_link','discord_profile_id','i_agree_to_terms_and_conditions')
        exclude =['created']

        widgets={
            'candidate' :forms.TextInput(attrs={'type':'hidden'}),
            'job' :forms.TextInput(attrs={'type':'hidden'}),

        }
