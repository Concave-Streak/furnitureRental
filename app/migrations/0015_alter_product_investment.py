# Generated by Django 4.0 on 2024-03-18 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_product_investment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='investment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
