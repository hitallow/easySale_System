from django import forms
from django.contrib import admin
from .models import User
from django.forms import (
    PasswordInput,TextInput, EmailInput)
import re

def validar_cpf(cpf: str) -> bool:

    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    if len(numbers) != 11:
        return False

    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True

class formCreation(forms.ModelForm):
    password = forms.CharField(label="Senha do lado", widget=forms.PasswordInput(attrs={'placeholder':'Sua senha', 'class':'form-control'}))
    password1 = forms.CharField(label="Confimação de senha", widget=PasswordInput(attrs={'placeholder':'Confime sua senha', 'class':'form-control'}))

    def clean_password1(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password1')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não batem")
        if len(password2)<8:
            raise forms.ValidationError("Sua senha é muito pequena, é indicado uma senha com mais de 8 caracteres")
        return password2

    def clean_cpf(self):

        cpf = str(self.cleaned_data.get('cpf'))

        if(not validar_cpf(cpf)):
            raise forms.ValidationError("CPF invalido")
        return cpf

    def save(self, commit=True):
        user = super(formCreation, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['is_active', 'is_admin','last_login']
        widgets = {
            'username': TextInput( attrs={'placeholder': 'Username','class':'form-control'}),
            'name':TextInput(attrs={'placeholder':'Seu nome','class':'form-control'}),
            'email':EmailInput(attrs={'class':'form-control','placeholder':'seunome@dominio.com'}),
            'cpf':TextInput(attrs={'class':'form-control'})
        }

class formLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']