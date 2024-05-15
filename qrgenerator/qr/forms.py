from django import forms
from . import models

class CreateQr (forms.ModelForm):
    class Meta:
        model = models.Qr
        fields = ['title', 'body', 'slug', 'image']

class MakeQr (forms.ModelForm):
    class Meta:
        model = models.Qr
        fields = ['title', 'body', 'slug', 'url']