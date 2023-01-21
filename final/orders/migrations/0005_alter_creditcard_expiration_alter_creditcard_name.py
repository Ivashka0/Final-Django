# Generated by Django 4.1.3 on 2023-01-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_creditcard_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='expiration',
            field=models.CharField(max_length=10000, verbose_name='Expiration'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='name',
            field=models.CharField(max_length=500000, verbose_name='Name'),
        ),
    ]
