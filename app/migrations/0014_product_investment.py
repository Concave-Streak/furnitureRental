# Generated by Django 4.0 on 2024-03-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_product_category_product_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='investment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]