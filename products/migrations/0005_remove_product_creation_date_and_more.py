# Generated by Django 4.0.1 on 2022-01-16 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_hidden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='modification_date',
        ),
    ]
