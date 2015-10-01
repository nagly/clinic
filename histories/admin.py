from django.contrib import admin
from patients.models import Patient

from histories.models import History
# Register your models here.

class HistoryAdmin(admin.ModelAdmin):
    class Meta:
        model = History
    list_display = ('patient_username', 'date')

    def patient_username(self, instance):
        return instance.patient.patient_username()
    patient_username.short_description = 'Username'

admin.site.register(History, HistoryAdmin)