# Generated by Django 4.2.1 on 2023-05-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0010_alter_author_author_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_firstname',
            field=models.CharField(default="Author's firstname", max_length=15, verbose_name='Author Name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_lastname',
            field=models.CharField(default="Author's lastname", max_length=15, verbose_name='Author Lastname'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(default='Genre name', max_length=30, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='publisher_name',
            field=models.CharField(default="Publisher's name", max_length=30, verbose_name='Publisher'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='serie_name',
            field=models.CharField(default='Serie name', max_length=40, verbose_name='Serie'),
        ),
    ]
