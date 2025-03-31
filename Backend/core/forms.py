from django import forms
from .models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserRegistration
        fields = ['full_name', 'phone_number', 'email', 'password']
