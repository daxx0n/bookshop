# Generated by Django 4.2.1 on 2023-06-28 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='orders.cart', verbose_name='Cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('Oformlen', 'Oformlen'), ('At_work', 'At_work'), ('Vydan', 'Vydan'), ('Closed', 'Closed')], default='NEW', max_length=8, verbose_name='Order status'),
        ),
    ]