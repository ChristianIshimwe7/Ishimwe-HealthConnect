# core/admin.py
from django.contrib import admin
from .models import Patient, UserRegistration, Doctor

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'weight', 'temperature', 'respiration_rate', 'service', 'hospital', 'doctor', 'medicine']
    list_filter = ['service', 'hospital', 'doctor']
    search_fields = ['name']

@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name']