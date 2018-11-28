from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','preco','datePost','cpfUserPost' , 'tipyDept']
    search_fields = ['id', 'name' , 'tipyDept']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product , ProductAdmin)
