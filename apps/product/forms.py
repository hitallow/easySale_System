from django import forms
from .models import Product
from django.forms import (
    NumberInput,TextInput, CheckboxInput,CheckboxSelectMultiple,Select,FileInput
    )


FAVORITE_COLORS_CHOICES = (
	('outros','Outros'),
    ('informatica', 'Informática'),
    ('som', 'Som'),
    ('roupas', 'Roupas'),
    ('computadores','Computadores'),
    ('comidas','comidas')

)
class InsertProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['cpfUserPost', 'slug']
        widgets = {
            'name': TextInput( attrs={'placeholder': 'nome do produto','class':'form-control'}),
            'description':TextInput(attrs={'placeholder':'Descrição do produto','class':'form-control'}),
            'preco':NumberInput(attrs={'placeholder':'Preco do produto','class':'form-control','min':'0.1'}),
            'juros':CheckboxInput(),
            'maxParc':NumberInput( attrs={'min':'1','max':'24' ,'class':'form-control'}),
            'tipyDept': Select(choices=FAVORITE_COLORS_CHOICES, attrs={'class':'custom-select'}),
            'image':FileInput(attrs={'class':'custom-file-input'}),
            'littleDescription' : TextInput(attrs={'placeholder':'digite uma pequena descrição do produto','class':'form-control', 'maxlength':'50'})

        }


class SeachProduto(forms.Form):
	nome = forms.CharField()
