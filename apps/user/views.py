from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from easySale_System import settings
from django.contrib import messages
from .forms import (formCreation, formLogin)
# Views da app User.
root ='user/'

#from django.contrib.auth import authenticate, login
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


def dashboard(request):
    return render(request , root+'profile.html')