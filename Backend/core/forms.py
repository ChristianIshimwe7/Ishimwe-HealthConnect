# core/forms.py
from django import forms
from django.contrib.auth.hashers import make_password
from .models import UserRegistration, Patient

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserRegistration
        fields = ['full_name', 'phone_number', 'email', 'password']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'weight', 'temperature', 'respiration_rate', 'service', 'hospital', 'doctor', 'medicine']