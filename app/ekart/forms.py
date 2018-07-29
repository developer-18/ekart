from django.forms import ModelForm
from django import forms
from .models import Cyclone
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class registration_form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = [
            'username', 'email', 'captcha', 'password'
        ]

class login_form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = [
            'username', 'password', 'captcha'
        ]

class cyclone_form(ModelForm):
    class Meta:
        model = Cyclone
        fields =[
            'cyclone_image'
        ]
        