from .models import Guest
from django import forms 

class GuestBoardForm(forms.ModelForm):
    
    class Meta:
        model = Guest
        fields = ['username', 'stdnum', 'message']