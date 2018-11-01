from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from apps.user.models import Product
def index(request):
    return render(request , 'home.html')

def login(request):
    return render(request , 'login.html')

def listAllProducts(request):
    produtos = Product.objects.all()
    context ={
        'produtos': produtos
    }
    return render(request ,'listProducts.html', context )