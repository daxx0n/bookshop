# Generated by Django 4.2.1 on 2023-06-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_books_book_age_books_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_quantity',
            field=models.PositiveIntegerField(blank=True, max_length=3, null=True, verbose_name='Age Restrictions'),
        ),
    ]
