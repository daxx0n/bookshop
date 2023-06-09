# Generated by Django 4.2.1 on 2023-06-20 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0014_alter_author_author_bio'),
        ('books', '0008_remove_books_book_author_books_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_author',
        ),
        migrations.AddField(
            model_name='books',
            name='book_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='directories.author', verbose_name='Author'),
        ),
    ]
