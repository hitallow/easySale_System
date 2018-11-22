from django.shortcuts import render

#from django.http import HttpResponse
# Views da app produto.

from .models import Product
def index(request):
    return render(request, 'home.html')


def listAllProducts(request):
    produtos = Product.objects.all()

    context ={
        'produtos': produtos
    }

    return render(request ,'listProducts.html', context)

def detail(request, slug):
    produto = Product.objects.get(slug=slug)
    context = {
        'produto':produto
    }
    return render(request , 'details.html', context)
