# Generated by Django 4.2.1 on 2023-06-21 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0014_alter_author_author_bio'),
        ('books', '0013_books_book_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='directories.genre', verbose_name='Genre'),
        ),
        migrations.AddField(
            model_name='books',
            name='book_year',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Year'),
        ),
    ]
