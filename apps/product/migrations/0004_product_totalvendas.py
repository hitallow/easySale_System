# Generated by Django 2.1.3 on 2018-12-06 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20181205_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='totalVendas',
            field=models.IntegerField(default=0, verbose_name='Total vendidos'),
        ),
    ]
