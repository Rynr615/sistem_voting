# user_registration/forms.py
from django import forms
from .models import UserRegistration

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

# user_registration/forms.py

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)




