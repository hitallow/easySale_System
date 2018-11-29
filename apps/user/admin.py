from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class MyUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'email']
    search_fields = ['name', 'cpf', 'email']
    # prepopulated_fields =

admin.site.register(User, MyUserAdmin)


