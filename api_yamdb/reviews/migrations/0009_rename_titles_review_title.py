# Generated by Django 3.2 on 2023-02-05 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20230205_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='titles',
            new_name='title',
        ),
    ]