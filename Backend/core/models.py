from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UserRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name

class Patient(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    temperature = models.FloatField()
    respiration_rate = models.PositiveIntegerField()
    service = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)
    medicine = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.age} y/o)"

    def categorize_age(self):
        if self.age <= 12:
            return "0 - 12"
        elif self.age <= 45:
            return "13 - 45"
        elif self.age <= 100:
            return "46 - 100"
        else:
            return "100 - Above"
        
      # core/models.py
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UserRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    temperature = models.FloatField()
    respiration_rate = models.PositiveIntegerField()
    service = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    medicine = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.age} y/o)"  