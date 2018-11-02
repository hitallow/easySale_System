from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def search(self , query):
        return self.get_queryset().filter( cpf__icontains=query  )




class User(models.Model):
    name = models.CharField('Nome do usuario' , null=False , blank=False , max_length=100)
    password = models.CharField('senha' , null=False , blank=False, max_length=15)
    cpf = models.IntegerField(verbose_name='CPF usuario' ,primary_key=True, unique=True)
    email = models.EmailField(unique=True, null=False , blank=False)
    objects = UserManager()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['name']

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