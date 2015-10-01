from django.contrib import admin

# Register your models here.
from doctors.models import Doctor

class DoctorAdmin(admin.ModelAdmin):
	class Meta:
		model = Doctor
	list_display = ('first_name', 'last_name')

admin.site.register(Doctor, DoctorAdmin)