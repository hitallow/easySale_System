from django.shortcuts import render
from django.http import HttpResponse

# Views da app User.
root ='user/'


def login(request):
    return render(request, root+'login.html')
