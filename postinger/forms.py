from django import forms
from .models import posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class postform(forms.ModelForm):
    
    class Meta:
        model = posts
        fields = ["caption","image"]
        # fields = ("caption","image")


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta :
        model = User
        fields = ("username","email","password1","password2")