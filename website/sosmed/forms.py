from  django import forms
from . import models

class Igforms(forms.ModelForm):
    class Meta:
        model = models.Instagram
        fields =[
            'nama',
            'username',
            'email'
        ]
