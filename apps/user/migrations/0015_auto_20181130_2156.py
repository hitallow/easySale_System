# Generated by Django 2.1.3 on 2018-11-30 21:56

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20181130_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=100, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Nome de usuario só pode conter letras, números ou estes caracteres: @/./+/_', 'invalid')], verbose_name='Nome de usuario'),
        ),
    ]