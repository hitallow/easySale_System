from django.db import models
from apps.user.models import User

# Modelos da app produto.

class Product(models.Model):
    id = models.IntegerField(primary_key=True )
    name = models.CharField('Nome do Produto' , max_length=50)
    preco = models.DecimalField(verbose_name='Preço do produto' , max_digits=10 , decimal_places=2)
    datePost = models.DateField('Postado em')
    cpfUserPost = models.ForeignKey(User, on_delete=models.CASCADE)
    tipyDept = models.CharField('Departamento' , null=False , blank=False , max_length=20)
    description = models.TextField('Descrição do produto' )
    juros = models.BooleanField( null=False , blank=False)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']