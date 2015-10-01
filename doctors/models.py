from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=120, null=False, blank=True)
    last_name = models.CharField(max_length=120, null=False, blank=True)
    pesel = models.CharField(max_length=11, null=False, blank=True)
    pwz = models.CharField(max_length=7)
    specialization = models.CharField(max_length=25)
    since = models.CharField(max_length=4)
    about = models.TextField()

    def __unicode__(self):
    	return smart_unicode(self.first_name + ' ' + self.last_name)