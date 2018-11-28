from django.urls import path, include
#from django.contrib.auth import authenticate
from apps.user import views
from django.contrib.auth.views import LoginView
app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    #path('login/', views.Login, name='login'),
    path('registrar-se/', views.register, name='register'),
    path('sair/',views.logoutview,name='logout')
]
