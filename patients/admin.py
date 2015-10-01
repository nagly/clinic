from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# Register your models here.
from patients.models import Patient

class PatientAdmin(admin.ModelAdmin):
    class Meta:
        model = Patient
    list_display = ('patient_username', 'patient_email', 'pesel')

    def patient_email(self, instance):
        return instance.user.email
    patient_email.short_description = 'Email'

    def patient_username(self, instance):
        return instance.user.username
    patient_username.short_description = 'Username'

admin.site.register(Patient, PatientAdmin)






# jakbym chcial zeby w adminie w Users byly pola z modelu Patient to odhaszowac
# class PatientInline(admin.StackedInline):
#     model = Patient
#     can_delete = False
#     verbose_name_plural = 'patients'

# class UserAdmin(UserAdmin):
#     inlines = (PatientInline, )

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
