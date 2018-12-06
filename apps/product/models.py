
from django.db import models
#from django.contrib.auth import get_user_model
from easySale_System import settings

#User = get_user_model()
class CustomManager(models.Manager):

    def getForName(self, name):
        return self.all().filter(name=name)

    def allProducts(self):
        return self.all()

    def getProductsForUser(self , user):
        return self.all().filter(cpfUserPost=user)

    def getSlug(self, slug):
        return self.all().filter(slug=slug)


class Product(models.Model):
    name = models.CharField('Nome do Produto' , max_length=50)
    slug = models.SlugField(unique=True)
    preco = models.DecimalField(verbose_name='Preço do produto' , max_digits=10 , decimal_places=2)
    datePost = models.DateField(auto_now_add=True)  
    tipyDept = models.CharField('Departamento' , null=False , blank=False , max_length=20)
    description = models.TextField('Descrição do produto',max_length=200 )
    littleDescription = models.TextField('Curta descrição',max_length=50 )
    juros = models.BooleanField( null=False , blank=False)
    image = models.ImageField(verbose_name="Imagem do Produto", upload_to='product/images',null=True, blank=True )
    maxParc = models.IntegerField(verbose_name='Total de Parcelas')
    cpfUserPost = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    totalVendas = models.IntegerField('Total vendidos',default=0,null=False)

    objects = CustomManager()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']



class Coment(models.Model):
    comentario = models.TextField('Comentário do produto',max_length=200 )
    nota = models.DecimalField('Nota', max_digits=10,decimal_places=1)
    title = models.TextField("Titulo do comentario",max_length=50)
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['nota']
