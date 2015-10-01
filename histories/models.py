from django.db import models
from patients.models import Patient

# Create your models here.
class History(models.Model):
    patient = models.ForeignKey('patients.Patient')
    date = models.DateField()
    text = models.TextField()

    def patient_username(self):
        return self.patient.patient_username()
