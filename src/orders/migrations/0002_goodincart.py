# Generated by Django 4.2.1 on 2023-06-27 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0029_alter_books_book_price'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantity')),
                ('price', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='Price')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='orders.cart', verbose_name='Cart')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.books', verbose_name='Good')),
            ],
        ),
    ]
