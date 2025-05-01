from .models import *
from django import forms


class GuestForm(forms.ModelForm):
    class Meta:
        model=Guest
        fields=['username', 'stdnum', 'message']