from django.test import TestCase
from .models import Patient

class PatientModelTest(TestCase):
    def setUp(self):
        # Create a sample Patient instance to test model functionality.
        self.patient = Patient.objects.create(
            name="John Doe",
            age=30,
            weight=75.0,
            temperature=37.0,
            respiration_rate=18,
            service="General Medicine",
            hospital="City Hospital",
            doctor="Dr. Smith",
            medicine="Paracetamol"
        )

    def test_patient_creation(self):
        """Test that a Patient instance is created with the correct attributes."""
        self.assertEqual(self.patient.name, "John Doe")
        self.assertEqual(self.patient.age, 30)
        self.assertEqual(self.patient.weight, 75.0)
        self.assertAlmostEqual(self.patient.temperature, 37.0)
        self.assertEqual(self.patient.respiration_rate, 18)
        self.assertEqual(self.patient.service, "General Medicine")
        self.assertEqual(self.patient.hospital, "City Hospital")
        self.assertEqual(self.patient.doctor, "Dr. Smith")
        self.assertEqual(self.patient.medicine, "Paracetamol")

    def test_str_representation(self):
        """Test the string representation of the Patient instance."""
        expected_str = "John Doe (30 y/o)"
        self.assertEqual(str(self.patient), expected_str)

    def test_to_dict_method(self):
        """Test that the to_dict method returns the correct dictionary representation."""
        expected_dict = {
            "name": "John Doe",
            "age": 30,
            "weight": 75.0,
            "temperature": 37.0,
            "respiration_rate": 18,
            "service": "General Medicine",
            "hospital": "City Hospital",
            "doctor": "Dr. Smith",
            "medicine": "Paracetamol"
        }
        self.assertEqual(self.patient.to_dict(), expected_dict)
