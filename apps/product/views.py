from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (InsertProduct)
from django.utils.text import slugify
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
            produto = form.save(commit=False)
            produto.slug = slugify(form.cleaned_data['name'])
            produto.cpfUserPost = request.user
            produto.save()
            return redirect('product:allProducts')
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
