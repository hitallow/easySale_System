from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import (InsertProduct)
#from django.http import HttpResponse
# Views da app produto.

from .models import Product
def index(request):
    return render(request, 'home.html')

@login_required()
def listAllProducts(request):
    produtos = Product.objects.all()

    context ={
        'produtos': produtos
    }

    return render(request ,'listProducts.html', context)
def cadastrar(request):
    if request.method == 'POST':
        form = InsertProduct(request.POST)
        if (form.is_valid()):
            print('Form flag')
            print(form.cleaned_data['slug'])
    else:
        print("form limpo")
        form = InsertProduct()
    context = {
        'form': form
    }
    return render(request, 'cadastra.html', context)

def detail(request, slug):
    produto = Product.objects.get(slug=slug)
    context = {
        'produto':produto
    }
    return render(request , 'details.html', context)
