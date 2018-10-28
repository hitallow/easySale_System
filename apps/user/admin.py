from django.contrib import admin
from .models import User, Product

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','cpf','email']
    search_fields = ['name' , 'cpf' , 'email']
   # prepopulated_fields =
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','preco','datePost','cpfUserPost' , 'tipyDept']
    search_fields = ['id', 'name' , 'tipyDept']
admin.site.register(User , UserAdmin)
admin.site.register(Product , ProductAdmin)
# Register your models here.

