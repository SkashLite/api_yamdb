# Generated by Django 3.2 on 2023-02-11 17:14

import api.validation
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20230211_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[api.validation.validate_year]),
        ),
    ]
