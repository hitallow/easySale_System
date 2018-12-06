from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from easySale_System import settings
from django.contrib import messages
from .forms import (formCreation, editAccount)

# Views da app User.
root ='user/'
from apps.product.models import (Product, CustomManager)

@login_required
def logoutview(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


def register(request):
    if request.method == "POST":
        form = formCreation(request.POST)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.SUCCESS, 'Cadastro feito com sucesso',extra_tags="alert alert-success")
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

def editAccount(request):
    if request.method == 'POST':
        print('post')
    else: 
        form = formCreation(instance=request.user)
    context = {
        'form' : form
    }
    return render(request, root+'register.html', context)
