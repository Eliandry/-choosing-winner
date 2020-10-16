from django import forms
from .models import *


class AddPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo']


class AddAvatar(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['avatar']
