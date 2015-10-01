# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from patients.models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'pesel', 'birth', 'street', 'house_no'] #dzieki temu forma rejestracji nie bedzie zawierac wszystkich pol z modelu patients tylko moje wybrane (np 'name')
        labels = {
        'birth': 'Data urodzenia (dd.mm.rrrr)',
        'first_name': 'Imię',
        'last_name': 'Nazwisko',
        'street': 'Ulica',
        'house_no': 'Dokładny numer domu (lokalu)',
        }
class EditPatientForm(forms.ModelForm):
    class Meta:
        model = Patient