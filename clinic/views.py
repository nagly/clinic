from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm <- jesli uzywamy podstawowej formy rejestracji uzytkownika
from forms import MyRegistrationForm
from doctors.models import Doctor

def home(request):
    
        context = {} #'user': User.objects.get(username=request.user.username)
        template = "home.html"
        return render(request, template, context)

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    #obiekt auth -> metoda authenticate -> sprawdza username i password,
    #jezeli znajdzie to zwraca obiekt user, jesli nie znajdzie, zwraca None

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

def loggedin(request):
    context = {'full_name': request.user.username}
    template = "loggedin.html"
    return render(request, template, context)

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = MyRegistrationForm()
    print args
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

def doctors_view(request):
    context = {'doctors': Doctor.objects.all()}
    template = "doctors.html"
    return render(request, template, context)