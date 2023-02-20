from django import forms
from .models import login, Register


class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'