# Generated by Django 4.1.3 on 2023-01-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_base64',
            field=models.CharField(blank=True, max_length=1000000),
        ),
    ]
