from django import forms
from .models import EducationModule



class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModule
        fields = '__all__'
