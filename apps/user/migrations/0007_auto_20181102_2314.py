# Generated by Django 2.1.2 on 2018-11-02 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_product_juros'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cpfUserPost',
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]