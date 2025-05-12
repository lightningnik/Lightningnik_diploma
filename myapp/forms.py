# myapp/forms.py
from django import forms
from .models import Diploma

class DiplomaForm(forms.ModelForm):
    class Meta:
        model = Diploma
        fields = ['title', 'issuer', 'date_issued', 'link'] # Проверьте имена полей здесь
        widgets = {
            'date_issued': forms.DateInput(attrs={'type': 'date'})
        }