from django import forms
from .models import AnonymousTalk


class AnonymousTalkForm(forms.ModelForm):
    class Meta:
        model = AnonymousTalk
        fields = ['talk']
        labels = {
            'talk' : 'talk'
        }