from django.forms import ModelForm
from django.forms.widgets import DateInput, NumberInput
from .models import Patient, Assessment
from django import forms
import datetime
from dateutil.relativedelta import relativedelta
from measurement.measures import Weight
from django_measurement.forms import MeasurementField


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
        return birthdate



class AssessmentForm(ModelForm):
    class Meta:
        model = Assessment
        exclude = ('patient',)
        widgets = {
            'visit_date': DateInput(attrs={'type': 'date'}),
            'height': NumberInput(attrs={'placeholder': 'In cm'}),
            'weight': NumberInput(attrs={'placeholder': 'In kgs'}),
            'temperature': NumberInput(attrs={'placeholder': 'In degrees celcius'}),
        }
    
    
    def clean_visit_date(self):
        visit_date = self.cleaned_data.get("visit_date")
        if visit_date > datetime.date.today():
            raise forms.ValidationError("The date cannot be greater than today's date")
            return visit_date
        return visit_date