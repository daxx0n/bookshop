# Generated by Django 4.2.1 on 2023-07-03 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_profile_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='group',
        ),
    ]
