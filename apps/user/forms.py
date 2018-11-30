from django import forms
from django.contrib import admin
from .models import User
from django.forms import PasswordInput,TextInput
import re



class formCreation(forms.ModelForm):
    password = forms.CharField(label="Senha do lado", widget=forms.PasswordInput(attrs={'placeholder':'Sua senha'}))
    password1 = forms.CharField(label="Confimação de senha", widget=PasswordInput(attrs={'placeholder':'Confime sua senha'}))

    def clean_password1(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password1')
        print(password1)
        print(password2)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não batem")
        return password2

    def clean_cpf(self):
        cpf = str(self.cleaned_data.get('cpf'))
        if(not (re.match('^((\d{3}).(\d{3}).(\d{3})-(\d{2}))*$', cpf) or re.match('^\d{11}$', cpf))):
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
            'username': TextInput( attrs={'placeholder': 'username'}),
            'name':TextInput(attrs={'placeholder':'Seu nome','class':'form-control'})
        }