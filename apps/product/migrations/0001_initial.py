# Generated by Django 2.1.2 on 2018-11-02 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0007_auto_20181102_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nome do Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço do produto')),
                ('datePost', models.DateField(verbose_name='Postado em')),
                ('tipyDept', models.CharField(max_length=20, verbose_name='Departamento')),
                ('description', models.TextField(verbose_name='Descrição do produto')),
                ('juros', models.BooleanField()),
                ('cpfUserPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'verbose_name_plural': 'Produtos',
                'verbose_name': 'Produto',
                'ordering': ['id'],
            },
        ),
    ]
