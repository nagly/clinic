from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
from patients.forms import PatientForm
from patients.models import Patient
from histories.models import History
from calendars.models import Hour, Date

def profile_view(request, id):
    try:
        context = {'user': User.objects.get(username=request.user.username), 'reserved': Hour.objects.extra(where=["patient_id = %u" %request.user.id]), 'dates': Date.objects.all(),
               'patient': Patient.objects.get(user_id=id)}
    except Patient.DoesNotExist:
        context = {'patient': None}
    template = "profile.html"
    return render(request, template, context)

def medical_card(request, id):
    
    form = PatientForm(request.POST or None)
    if form.is_valid():
        new_patient = form.save(commit=False)
        new_patient.user_id = request.user.id #dzieki temu zalogowany uzytkownik bedzie mogl zalozyc karte pacjenta wswoim profilu, nie bedzie wyboru userow, do bazy bedzie wpisany user ktory zrequestowal zadanie
        new_patient.save()
        return HttpResponseRedirect('/')
    try:
        context = {'patient': Patient.objects.get(user_id=id), "forma_pacjenta":form}
    except Patient.DoesNotExist:
        context = {'patient': None, 'forma_pacjenta':form}


    
    template = "medical_card.html"
    return render(request, template, context)

def history(request, id):
    context={'history': History.objects.extra(where=["patient_id = %s" %id]), 'user': User.objects.get(username=request.user.username),
             'history_count': History.objects.extra(where=["patient_id = %s" %id]).count()}
    template="history.html"
    return render(request, template, context)

# def profile(request, id): #to jest widok strony profilu uzytkownika. Kazdy moze wpisac url uzytkownika i wyswietla mu sie informacje o danym userze
#     context = {'pacjent': User.objects.get(id=id)}
#     template = "profile2.html"
#     return render(request, template, context)