# Generated by Django 3.2 on 2023-02-09 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('id',), 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
    ]