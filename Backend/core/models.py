from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    temperature = models.FloatField()
    respiration_rate = models.PositiveIntegerField()
    service = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)
    doctor = models.CharField(max_length=255)
    medicine = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.age} y/o)"

    def to_dict(self):
        """
        Returns a dictionary representation of the Patient instance.
        This can be useful for serializing the object manually.
        """
        return {
            "name": self.name,
            "age": self.age,
            "weight": self.weight,
            "temperature": self.temperature,
            "respiration_rate": self.respiration_rate,
            "service": self.service,
            "hospital": self.hospital,
            "doctor": self.doctor,
            "medicine": self.medicine,
        }







class UserRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
