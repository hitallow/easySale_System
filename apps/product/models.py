from django.db import models
from apps.user.models import User

# Modelos da app produto.

class Product(models.Model):
    name = models.CharField('Nome do Produto' , max_length=50)
    slug = models.SlugField(unique=True)
    preco = models.DecimalField(verbose_name='Preço do produto' , max_digits=10 , decimal_places=2)
    datePost = models.DateField(auto_now_add=True)
    cpfUserPost = models.ForeignKey(User, on_delete=models.CASCADE)
    tipyDept = models.CharField('Departamento' , null=False , blank=False , max_length=20)
    description = models.TextField('Descrição do produto' )
    juros = models.BooleanField( null=False , blank=False)
    image = models.ImageField(verbose_name="Imagem do Produto", upload_to='product/images',null=True, blank=True )
    maxParc = models.IntegerField(verbose_name='Total de Parcelas')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']
