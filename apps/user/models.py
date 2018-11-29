from django.db import models

from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,AbstractUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None,is_Admin=False):
        if not email:
            raise TypeError('Informe um email')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        #password = make_password(password)
        user.set_password(password)
        user.date_joined = datetime.now()
        user.is_active = True
        if(is_Admin):
            return user
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        print(password)
        if password is None:
            raise TypeError('Você precisa de uma senha')
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            is_Admin=True
        )
        user.is_admin = True
        print(user.password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("Nome de usuario",null=False, blank=False, max_length=100, unique=True,default='')
    email = models.EmailField("Email", unique=True, null=False, blank=False)
    name = models.CharField('Nome completo' , null=False , blank=False , max_length=100)
    cpf = models.IntegerField('CPF usuario', primary_key=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.name

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']


