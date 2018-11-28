from django import forms
from .models import Product


class InsertProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['cpfUserPost', 'slug']


