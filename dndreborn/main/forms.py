from django import forms
from django.forms import ModelForm
from .models import Character


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['user', 'name', 'image', 'race', 'char_class', 'background', 'alignment']

