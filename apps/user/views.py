from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from easySale_System import settings

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
            return redirect(settings.LOGIN_URL)
    else:
        form = formCreation()

    context = {
        'form': form
    }
    return render(request, root+'register.html', context)


def loginInSite(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('sucesso')
            login(request, user)
            # Redirect to a success page.
            return redirect('product:index')
        else:
            print("falhou")
            # Return an 'invalid login' error message.
            ...
    else:
        form = formLogin()
        context = {
            'form' : form
        }
    return render(request, root+'login.html',context)