from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import formCreation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from easySale_System import settings
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
            signup = form.save(commit=False)
            signup.password = make_password(form.cleaned_data['password'])
            signup.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = formCreation()

    context = {
        'form': form
    }
    return render(request, root+'register.html', context)
