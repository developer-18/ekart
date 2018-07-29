from django.forms import ModelForm
from django import forms
from .models import Food
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class food_form(ModelForm):
    class Meta:
        model = Food
        fields =[
            'food_title', 'price', 'food_logo'
        ]
        
# class song_form(ModelForm):
#     class Meta:
#         model = Song
#         fields = [
#             'song_title', 'audio_file'
#         ]

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
    # def get_absolute_url(self):
    #     return reverse('music:user_login')
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = [
            'username', 'password', 'captcha'
        ]