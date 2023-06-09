# Generated by Django 4.2.1 on 2023-06-20 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0014_alter_author_author_bio'),
        ('books', '0002_rename_price_books_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='directories.author', verbose_name='Author'),
            preserve_default=False,
        ),
    ]
