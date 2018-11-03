from django.urls import path
from apps.user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
]