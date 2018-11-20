from django.urls import path
from apps.product import views

app_name = 'product'

urlpatterns = [
    path('', views.index , name='index'),
    path('products/', views.listAllProducts, name='allProducts')
]