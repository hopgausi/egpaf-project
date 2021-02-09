from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import Patient
from django import forms
import datetime
from dateutil.relativedelta import relativedelta


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'}),
        }
    
    def clean_birthdate(self):
        birthdate = self.cleaned_data.get("birthdate")
        if birthdate > datetime.date.today():
            raise forms.ValidationError("The date cannot be greater than today's date")
            return birthdate
        if birthdate < (datetime.date.today()-relativedelta(years=115)):
            raise forms.ValidationError(f"The date cannot be less than {datetime.date.today()-relativedelta(years=+115)}")
            return birthdate
