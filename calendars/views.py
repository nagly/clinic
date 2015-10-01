# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from calendars.models import Hour, Date
from patients.models import Patient
# Create your views here.


def hours(request):
    context = {'dates': Date.objects.all(),
               'months': Date.objects.dates('date', 'month'),
              }
    template = "calendar.html"
    return render(request, template, context)

def hour(request, id=1):
    context = {'hour': Hour.objects.get(id = id) }
    return render_to_response('hour.html', context)

def add_patient(request, id):
    if id:
        typed_hour = Hour.objects.get(id = id)
        new_patient = typed_hour.patient_id
        new_patient = request.user.id
        typed_hour.patient_id = new_patient
        typed_hour.save()
        messages.success(request, 'Zostałeś zapisany na wizytę, informacja o wizytach znajduje się na stronie głównej Twojego profilu')
    return HttpResponseRedirect('/calendar/all/')
    #return HttpResponseRedirect('/calendar/get/%s' %id)

def date(request, id):
    context = {'hours': Hour.objects.extra(where=["date_id = %s" %id]),
                'doctor': Date.objects.get(id = id),
                'patient': Patient.objects.get(user_id=request.user.id), #musi być request.user.id a nie samo id, bo sid odnosi sie do id dnia (date.id)
                'reserved': Hour.objects.extra(where=["date_id = %s" %id, "patient_id = %u" %request.user.id]).count()}
    template = "day.html"
    return render(request, template, context)

def signout(request, id_godz):
    hour = Hour.objects.get(id=id_godz)
    none_patient = None
    hour.patient_id = none_patient
    hour.save()
    messages.success(request, 'Zostałeś wypisany z wizyty')
    return HttpResponseRedirect('/users/%s/' %request.user.id)
