from django import forms

class LoginForm(forms.Form):                             #不能为空
    username = forms.CharField(max_length=12, min_length=6,required=True,error_messages={"required":'用户账号不能为空', 'invalid':'格式错误'},widget=forms.TextInput(attrs={"class":"c"}))
    passwd   = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'email'
        ]

