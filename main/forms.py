from django import forms
from .models import Talk


class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ['name','talk','email']
        labels = { 'name' :'name'  , 'talk' : 'talk'  ,  'email' :'email'}