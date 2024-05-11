# Generated by Django 4.2.7 on 2024-05-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='regular_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='selected_countries',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='shipping',
            field=models.CharField(choices=[('seller', 'Fullfilled by Seller'), ('ecom', 'Fullfilled by ECOM')], max_length=100),
        ),
    ]
