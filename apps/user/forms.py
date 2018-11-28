from django import forms
from django.contrib import admin
from .models import User
from django.forms import PasswordInput



class formCreation(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['is_active', 'is_admin','last_login']
        widgets = {
            'password': PasswordInput(),
        }
