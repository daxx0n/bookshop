# Generated by Django 4.2.1 on 2023-06-20 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0014_alter_author_author_bio'),
        ('books', '0009_remove_books_book_author_books_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_author',
        ),
        migrations.AddField(
            model_name='books',
            name='book_author',
            field=models.ManyToManyField(blank=True, null=True, to='directories.author', verbose_name='Author'),
        ),
    ]
