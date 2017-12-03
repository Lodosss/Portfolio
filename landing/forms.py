from django import forms
from .models import *


class SubscruberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ("Имя","email")