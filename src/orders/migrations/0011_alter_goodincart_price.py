# Generated by Django 4.2.1 on 2023-07-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodincart',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price'),
        ),
    ]
