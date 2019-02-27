from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from easySale_System import settings
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import (formCreation, editAccount)
from django.shortcuts import get_object_or_404
# Views da app User.
root ='user/'
from apps.product.models import (Product, CustomManager)
from .models import User
@login_required
def logoutview(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


def register(request):
    if request.method == "POST":
        form = formCreation(request.POST)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.SUCCESS, 'Cadastro feito com sucesso, faça login',extra_tags="alert alert-success")
            return redirect(settings.LOGIN_URL)
    else:
        form = formCreation()

    context = {
        'form': form
    }
    return render(request, root+'register.html', context)


@login_required
def dashboard(request):
    return render(request , root+'profile.html')


@login_required
def productOfClient(request):
    print('oi')
    produtos = Product.objects.getProductsForUser(request.user)
    print("dois")
    context =  {
        'produtos' : produtos
    }
    return render(request, root+'meus-produtos.html', context)

@login_required
def editAccount(request):
    context = {}

    if request.method == 'POST':
        print(form.cleaned_data['username'])
        print(form.cleaned_data['cpf'])
        print(form.cleaned_data['name'])

        if form.is_valid():
            #form.save()
            context['success'] = True
    else:
        form = editAccount()
    context['form'] = form
    return render(request, root+'editinformation.html', context)

@login_required
def editPassword(request):
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST , user = request.user)
        if form.is_valid():
            form.save()
            context['success'] = True

    else:
        form = PasswordChangeForm(user = request.user)
    context['form'] = form
    return render(request , root+'edit_password.html',context)