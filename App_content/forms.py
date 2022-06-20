from django import forms
from App_content.models import *


class PodcastModelForm(forms.ModelForm):
    class Meta:
        model = PodcastModel
        exclude = ['host', 'status']
