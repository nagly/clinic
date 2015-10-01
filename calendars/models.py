from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class Date(models.Model):
    date = models.DateField()
    doctor = models.ForeignKey('doctors.Doctor')

    def __unicode__(self):
        return smart_unicode(self.date)

class Hour(models.Model):    
    hour = models.CharField(max_length=5)    
    date = models.ForeignKey('Date')    
    patient = models.ForeignKey('patients.Patient', null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.hour)

    #magia, musze to ogarnac, najpierw ta funkcja w modelu
    #a potem w admin.py
    def current_doctor(self):
        return self.date.doctor
