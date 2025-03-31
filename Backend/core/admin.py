from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'weight',
        'temperature',
        'respiration_rate',
        'service',
        'hospital',
        'doctor',
        'medicine',
    )
