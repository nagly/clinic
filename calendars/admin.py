from django.contrib import admin

# Register your models here.
from calendars.models import Date, Hour

class DateAdmin(admin.ModelAdmin):
    class Meta:
        model = Date
    list_display = ('date', 'doctor')

admin.site.register(Date, DateAdmin)


class HourAdmin(admin.ModelAdmin):
    class Meta:
        model = Hour
    fields = ['hour', 'date', 'patient'] #dzieki temu przy tworzeniu nowej godziny lekarz nie bedzie mial widocznego pola 'pacjent', bo mu to niepotrzebne :)
    list_display = ('hour', 'date', 'current_doctor', 'patient')
    
    #tutaj jest druga czesc tej funkcji ktora pozwala wypisac kolumne
    #z innej tabeli w panelu admina
    def current_doctor(self, instance):
        return instance.date.doctor
    current_doctor.short_description = 'Doctor'



admin.site.register(Hour, HourAdmin)