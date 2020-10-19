from django import forms
from .models import *


class AddPhotoForm(forms.Form):
    photo = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))

class AddAvatar(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['avatar']
