# Generated by Django 4.2.1 on 2023-06-22 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0025_alter_books_book_price_alter_books_book_weight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 22, 13, 41, 52, 519395, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 22, 13, 41, 55, 451838, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
