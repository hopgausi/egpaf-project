from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput
from django.forms import ModelForm
from django import forms 


class UserRegistrationForm(UserCreationForm, ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1', 'password2']
        
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True, max_length=100)