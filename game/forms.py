from django.forms import ModelForm
from django import forms

from .models import *


class profile_edit(ModelForm):
    class Meta:
        model=player()
        fields='__all__'
        exclude=['user_name','points']