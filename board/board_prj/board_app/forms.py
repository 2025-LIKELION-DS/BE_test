from .models import Guest
from django import forms # !모델연결

class Form(forms.ModelForm): #forms.ModelForm
    class Meta:
        model = Guest # 모델명시
        fields = ["username", "stdnum", "message"]