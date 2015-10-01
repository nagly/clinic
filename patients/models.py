from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    pesel = models.CharField(max_length=11)
    birth = models.DateField()
    street = models.CharField(max_length=50)
    house_no = models.CharField(max_length=10)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    insurance = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.user.username)

    def patient_username(self):
        return self.user.username

    def patient_email(self):
        return self.user.email
