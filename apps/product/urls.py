from django.urls import path
from apps.product import views

app_name = 'product'

urlpatterns = [
    path('', views.index , name='index'),
    path('produtos/', views.listAllProducts, name='allProducts'),
    path('produtos/<slug:slug>/', views.detail, name='details-product'),
    path('cadastrar',views.cadastrar, name='cadastrar'),
    path('editar/<slug:slug>',views.editProduto, name='editProduct')
]
