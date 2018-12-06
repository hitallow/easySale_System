from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (InsertProduct)
from django.utils.text import slugify
from django.contrib import messages
#from django.http import HttpResponse
# Views da app produto.

from .models import Product
def index(request):
    return render(request, 'home.html')


def listAllProducts(request):
    produtos = Product.objects.allProducts()


    context ={
        'produtos': produtos
    }

    return render(request ,'listProducts.html', context)
@login_required()
def cadastrar(request):
    if request.method == 'POST':
        form = InsertProduct(request.POST)
        if (form.is_valid()):
            produto = form.save(commit=False)
            produto.slug = slugify(form.cleaned_data['name'])
            produto.cpfUserPost = request.user
            produto.save()
            messages.add_message(request, messages.INFO, 'Hello world.')
            return redirect('product:allProducts')
    else:
        form = InsertProduct()
    context = {
        'form': form
    }
    return render(request, 'cadastra.html', context)

def detail(request, slug):
    produto = Product.objects.get(slug=slug)
    produto.parcelas = round(produto.preco/produto.maxParc , 2)
    context = {
        'produto':produto
    }
    return render(request , 'details.html', context)

def searchName(request, name):
    produtos = Product.objects.searchName(name=name)
    context = {
        'produtos': produtos
    }
    return render(request, templantename , context)


