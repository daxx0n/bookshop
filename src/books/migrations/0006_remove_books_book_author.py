# Generated by Django 4.2.1 on 2023-06-20 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_books_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_author',
        ),
    ]