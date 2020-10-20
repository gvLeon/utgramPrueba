""" User profile form """

# Django
from django import forms

class ProfileForm(forms.Form):
    """Profile form """
    website = forms.URLField(max_length=200, required=True)
    bio =     forms.CharField(max_length=800,required=True)
    picture = forms.ImageField()