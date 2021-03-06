from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        #user.is_staff = True   #<--w auth.models w modelu User. Tworzy nam uzytkownika ktory moze wejsc do panelu admina, ale nie ma jeszcze zadnych praw

        if commit:
            user.save()

        return user