# Generated by Django 2.0.5 on 2018-05-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20161130_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_top',
            field=models.BooleanField(default=False),
        ),
    ]
