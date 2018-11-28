from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import formCreation
# Views da app User.
root ='user/'


def register(request):
    if request.method == "POST":
        print('ENTROU AQUI 1 ')
        form = formCreation(request.POST)
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            signup = form.save(commit=False)
            signup.password = make_password(form.cleaned_data['password'])
            signup.save()
            return redirect("user:login")

    else:
        print('ENTROU AQUI 2 ')
        form = formCreation()

    context = {
        'form': form
    }
    return render(request, root+'register.html', context)
