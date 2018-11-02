from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','cpf','email']
    search_fields = ['name' , 'cpf' , 'email']
   # prepopulated_fields =



admin.site.register(User , UserAdmin)

# Register your models here.

