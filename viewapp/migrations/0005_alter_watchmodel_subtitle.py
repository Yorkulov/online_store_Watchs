# Generated by Django 4.1 on 2023-04-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewapp', '0004_contactmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchmodel',
            name='subtitle',
            field=models.CharField(max_length=150),
        ),
    ]
